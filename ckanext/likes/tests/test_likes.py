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

"""Tests for plugin.py."""

from ckanext.likes.actions import like_dataset, has_liked_dataset, \
                                dislike_dataset, dataset_likes_counter, \
                                like_resource, has_liked_resource, dislike_resource, \
                                resource_likes_counter

import ckan.logic as logic
import ckan.tests.factories as factories
import mock
import ckan.plugins.toolkit as toolkit
import ckan.tests.helpers as helpers
from ckan import model
from ckan.plugins import toolkit

import pdb
import pytest



# MUST HAVE pytest-ckan installed
# RUN WITHOUT warmings: pytest --ckan-ini=test.ini --disable-pytest-warnings
# RUN WITH print(): pytext --ckan-ini=test.ini -s

@pytest.mark.ckan_config("ckan.plguins", "likes")
@pytest.mark.usefixtures("with_plugins")
@pytest.mark.usefixtures("clean_db")
class TestLikes(object):

    def test_user_likes_dataset(self, app):

        user = factories.User(name='bob', email='bob@gmail.com')
        pkg = factories.Dataset(creator_user_id=user['id'])
        pkg.update(dataset_id=pkg['id'])

        auth_user_obj = model.User.get(user['id'])

        context= {'user': user['id'],
                  'auth_user_obj': auth_user_obj,
                  'ignore_auth': True

        }

        result = like_dataset(context=context, data_dict=pkg)
        assert result == "This user has successfully liked this dataset."



    def test_user_has_liked_dataset(self, app):

        user = factories.User(name='bob', email='bob@gmail.com')
        pkg = factories.Dataset(creator_user_id=user['id'])
        pkg.update(dataset_id=pkg['id'])

        auth_user_obj = model.User.get(user['id'])

        context= {'user': user['id'],
                  'auth_user_obj': auth_user_obj,
                  'ignore_auth': True

        }

        liked = like_dataset(context=context, data_dict=pkg)

        result = has_liked_dataset(context=context, data_dict=pkg)
        assert result == True
        

    def test_user_dislike_dataset(self, app):

        user = factories.User(name='bob', email='bob@gmail.com')
        pkg = factories.Dataset(creator_user_id=user['id'])
        pkg.update(dataset_id=pkg['id'])

        auth_user_obj = model.User.get(user['id'])

        context= {'user': user['id'],
                  'auth_user_obj': auth_user_obj,
                  'ignore_auth': True

        }

        liked = like_dataset(context=context, data_dict=pkg)

        result = dislike_dataset(context=context, data_dict=pkg)
        assert result == "This user has successfully disliked this dataset."

    def test_like_counter_dateset(self, app):

        user = factories.User(name='bob', email='bob@gmail.com')
        pkg = factories.Dataset(creator_user_id=user['id'])
        pkg.update(dataset_id=pkg['id'])

        auth_user_obj = model.User.get(user['id'])

        context= {'user': user['id'],
                  'auth_user_obj': auth_user_obj,
                  'ignore_auth': True

        }

        liked = like_dataset(context=context, data_dict=pkg)
        result = dataset_likes_counter(context=context, data_dict=pkg)
        assert result == 1

    def test_user_likes_resoruce(self, app):
        user = factories.User(name='bob', email='bob@gmail.com')
        pkg = factories.Dataset(creator_user_id=user['id'])
        pkg.update(dataset_id=pkg['id'])

        resource = factories.Resource(package_id=pkg['dataset_id'], url='http://example.com', format='CSV')
        resource.update(resource_id=resource['id'])
        auth_user_obj = model.User.get(user['id'])

        context= {'user': user['id'],
                  'auth_user_obj': auth_user_obj,
                  'ignore_auth': True}

        result = like_resource(context=context, data_dict=resource)
        assert result == 'This user has successfully liked this resource.'

    def test_user_has_liked_resoruce(self, app):

        user = factories.User(name='bob', email='bob@gmail.com')
        pkg = factories.Dataset(creator_user_id=user['id'])
        pkg.update(dataset_id=pkg['id'])

        resource = factories.Resource(package_id=pkg['dataset_id'], url='http://example.com', format='CSV')
        resource.update(resource_id=resource['id'])

        auth_user_obj = model.User.get(user['id'])

        context= {'user': user['id'],
                  'auth_user_obj': auth_user_obj,
                  'ignore_auth': True

        }

        liked = like_resource(context=context, data_dict=resource)

        result = has_liked_resource(context=context, data_dict=resource)
        assert result == True

    def test_user_has_disliked_resource(self, app):

        user = factories.User(name='bob', email='bob@gmail.com')
        pkg = factories.Dataset(creator_user_id=user['id'])
        pkg.update(dataset_id=pkg['id'])

        resource = factories.Resource(package_id=pkg['dataset_id'], url='http://example.com', format='CSV')
        resource.update(resource_id=resource['id'])
        auth_user_obj = model.User.get(user['id'])

        context= {'user': user['id'],
                  'auth_user_obj': auth_user_obj,
                  'ignore_auth': True}

        liked = like_resource(context=context, data_dict=resource)
        result = dislike_resource(context=context, data_dict=resource)
        assert result == "This user has successfully disliked this resource."

    def test_resource_likes_counter(self, app):

        user = factories.User(name='bob', email='bob@gmail.com')
        pkg = factories.Dataset(creator_user_id=user['id'])
        pkg.update(dataset_id=pkg['id'])

        resource = factories.Resource(package_id=pkg['dataset_id'], url='http://example.com', format='CSV')
        resource.update(resource_id=resource['id'])

        auth_user_obj = model.User.get(user['id'])

        context= {'user': user['id'],
                  'auth_user_obj': auth_user_obj,
                  'ignore_auth': True

        }

        liked = like_resource(context=context, data_dict=resource)
        result = resource_likes_counter(context=context, data_dict=resource)
        assert result == 1

