import datetime
from ckan.model.domain_object import DomainObject
from ckan.model.meta import Session, mapper, metadata
from ckan.model.types import make_uuid
from sqlalchemy import Column, ForeignKey, Table, types

user_likes_dataset_table = None
user_likes_resource_table = None

def setup():
    if user_likes_dataset_table is None:
        define_user_likes_dataset_table()

    if user_likes_resource_table is None:
        define_user_likes_resource_table()

    if not user_likes_dataset_table.exists():
        user_likes_dataset_table.create()

    if not user_likes_resource_table.exists():
        user_likes_resource_table.create()


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
    def insert(self, like):
        Session.add(like)
        Session.commit()

        return like

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
    def insert(self, like):
        Session.add(like)
        Session.commit()

        return like

    @classmethod
    def delete(self, obj):
        deleted = Session.delete(obj)
        Session.commit()
        return deleted

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