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
    
    if user_likes_requests_table is None:
        define_user_likes_requests_table()

    if not user_likes_dataset_table.exists():
        user_likes_dataset_table.create()

    if not user_likes_resource_table.exists():
        user_likes_resource_table.create()
    
    if not user_likes_requests_table.exists():
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
        query = Session.query(self).autoflush(False)
        query = query.filter_by(**kwargs).first()

        return query

    @classmethod
    def total_likes(self, request_id):
        query = Session.query(self).autoflush(False)
        query = query.filter_by(resource_id=resource_id).count()

        return query

    @classmethod
    def delete(self, obj):
        deleted = Session.delete(obj)
        Session.commit()
        
        return deleted

    @classmethod
    def total_likes_for_requests(self, requests_list, user_id=None):
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


def define_user_likes_requests_table():
    global user_likes_requests_table

    user_likes_requests_table = Table(
        'user_likes_requests',
        metadata,
        Column('id', types.UnicodeText, primary_key=True, default=make_uuid),
        Column('user_id', types.UnicodeText, ForeignKey('user.id', ondelete='CASCADE'), nullable=False),
        Column('request_id', types.UnicodeText, ForeignKey('ckanext_requestdata_requests.id', ondelete='CASCADE'), nullable=False)
    )

    mapper(LikeRequests, user_likes_requests_table)