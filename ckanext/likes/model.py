"""
Copyright (c) 2018 Keitaro AB

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as
published by the Free Software Foundation, either version 3 of the
License, or (at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""

import datetime
from ckan.model.domain_object import DomainObject
from ckan.model.meta import Session, mapper, metadata
from ckan.model.types import make_uuid
from sqlalchemy import Column, ForeignKey, Table, types, func

user_likes_dataset_table = None
user_likes_resource_table = None
user_likes_requests_table = None

_ckanext_request_data_check = False
_RequestDataResource = None

def setup():
    if user_likes_dataset_table is None:
        define_user_likes_dataset_table()

    if user_likes_resource_table is None:
        define_user_likes_resource_table()
    
    if ckanext_requestdat_requests_exists() and user_likes_requests_table is None:
        define_user_likes_requests_table()

    if not user_likes_dataset_table.exists():
        user_likes_dataset_table.create()

    if not user_likes_resource_table.exists():
        user_likes_resource_table.create()
    
    if ckanext_requestdat_requests_exists() and not user_likes_requests_table.exists():
        user_likes_requests_table.create()



class LikeDataset(DomainObject):
    @classmethod
    def get(self, **kwargs): 
        query = Session.query(self).autoflush(False)
        query = query.filter_by(**kwargs).first()

        return query
    
    @classmethod
    def total_likes(self, dataset_id):
        query = Session.query(self).autoflush(False)
        query = query.filter_by(dataset_id=dataset_id).count()

        return query

    @classmethod
    def delete(self, obj):
        deleted = Session.delete(obj)
        Session.commit()

        return deleted

class LikeResource(DomainObject):
    @classmethod
    def get(self, **kwargs):
        query = Session.query(self).autoflush(False)
        query = query.filter_by(**kwargs).first()

        return query

    @classmethod
    def total_likes(self, resource_id):
        query = Session.query(self).autoflush(False)
        query = query.filter_by(resource_id=resource_id).count()

        return query

    @classmethod
    def delete(self, obj):
        deleted = Session.delete(obj)
        Session.commit()
        
        return deleted


class LikeRequests(DomainObject):

    @classmethod
    def get(self, **kwargs):
        define_request_data_model()
        query = Session.query(self).autoflush(False)
        query = query.filter_by(**kwargs).first()

        return query

    @classmethod
    def total_likes(self, request_id):
        define_request_data_model()
        query = Session.query(self).autoflush(False)
        query = query.filter_by(resource_id=resource_id).count()

        return query

    @classmethod
    def delete(self, obj):
        define_request_data_model()
        deleted = Session.delete(obj)
        Session.commit()
        
        return deleted

    @classmethod
    def total_likes_for_requests(self, requests_list, user_id=None):
        define_request_data_model()
        query = Session.query(LikeRequests.request_id, func.count(LikeRequests.request_id)).autoflush(False)
        query = query.filter(LikeRequests.request_id.in_(requests_list)).group_by(LikeRequests.request_id)
        if user_id:
            query = query.filter_by(user_id=user_id)
        
        result = query.all()

        likes = {}
        for r in result:
            likes[str(r[0])] = r[1]
        return likes


def get_request(request_id):
    global _ckanext_request_data_check
    global _RequestDataResource

    if not _ckanext_request_data_check:
        try:
            from ckanext.requestdata.model import ckanextRequestdata
            _RequestDataResource = ckanextRequestdata
        except ImportError:
            pass
        finally:
            _ckanext_request_data_check = True

    if not _RequestDataResource:
        return None
    
    return _RequestDataResource.get(id=request_id)


def define_user_likes_dataset_table():
    global user_likes_dataset_table

    user_likes_dataset_table = Table(
        'user_likes_dataset',
        metadata,
        Column('id', types.UnicodeText, primary_key=True, default=make_uuid),
        Column('user_id', types.UnicodeText, ForeignKey('user.id', ondelete='CASCADE'), nullable=True),
        Column('dataset_id', types.UnicodeText, ForeignKey('package.id', ondelete='CASCADE'), nullable=True),
    )

    mapper(LikeDataset, user_likes_dataset_table)


def define_user_likes_resource_table():
    global user_likes_resource_table

    user_likes_resource_table = Table(
        'user_likes_resource',
        metadata,
        Column('id', types.UnicodeText, primary_key=True, default=make_uuid),
        Column('user_id', types.UnicodeText, ForeignKey('user.id', ondelete='CASCADE'), nullable=True),
        Column('resource_id', types.UnicodeText, ForeignKey('resource.id', ondelete='CASCADE'), nullable=True),
    )

    mapper(LikeResource, user_likes_resource_table)


def define_user_likes_requests_table(foreign_key_to_requestdata=True):
    global user_likes_requests_table

    if foreign_key_to_requestdata:
        user_likes_requests_table = Table(
            'user_likes_requests',
            metadata,
            Column('id', types.UnicodeText, primary_key=True, default=make_uuid),
            Column('user_id', types.UnicodeText, ForeignKey('user.id', ondelete='CASCADE'), nullable=False),
            Column('request_id', types.UnicodeText, ForeignKey('ckanext_requestdata_requests.id', ondelete='CASCADE'), nullable=False)
        )
    else:
        user_likes_requests_table = Table(
            'user_likes_requests',
            metadata,
            Column('id', types.UnicodeText, primary_key=True, default=make_uuid),
            Column('user_id', types.UnicodeText, ForeignKey('user.id', ondelete='CASCADE'), nullable=False),
            Column('request_id', types.UnicodeText, nullable=False, index=True)
        )

    mapper(LikeRequests, user_likes_requests_table)


def ckanext_requestdat_requests_exists():
    try:
        from ckanext.requestdata.model import request_data_table
        return request_data_table is not None
    except ImportError:
        pass
    return False


def define_request_data_model():
    global user_likes_requests_table

    if user_likes_requests_table is None:
        use_foreign_key_to_requestsdata = ckanext_requestdat_requests_exists()
        define_user_likes_requests_table(use_foreign_key_to_requestsdata)
        if not user_likes_requests_table.exists():
            user_likes_requests_table.create()

