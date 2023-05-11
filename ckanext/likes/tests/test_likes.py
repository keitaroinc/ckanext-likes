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

from ckanext.likes.actions import like_dataset, has_liked_dataset, dislike_dataset
# from ckanext.likes.model import LikeDataset, LikeResource, LikeRequests
import ckan.logic as logiv
import ckan.tests.factories as factories
import mock
import ckan.plugins.toolkit as toolkit
import ckan.tests.helpers as helpers
from ckan import model
from ckan.plugins import toolkit

import pdb
import pytest
import six


# MUST HAVE pytest-ckan installed
# RUN WITHOUT warmings: pytest --ckan-ini=test.ini --disable-pytest-warnings
# RUN WITH print(): pytext --ckan-ini=test.ini -s

@pytest.mark.ckan_config("ckan.plguins", "likes")
@pytest.mark.usefixtures("with_plugins")
@pytest.mark.usefixtures("clean_db")
class TestLikes(object):

    def like_dataset():
        user = factories.User(name='bob', email='bob@gmail.com')
        pkg = factories.Dataset(creator_user_id=user['id'])
        pkg.update(dataset_id=pkg['id'])

        auth_user_obj = model.User.get(user['id'])

        context= {'user': user['id'],
                  'auth_user_obj': auth_user_obj,
                  'ignore_auth': True

        }

        result = like_dataset(context=context, data_dict=pkg)
        return result   


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


    # def test_like_dataset_empty_dict(app):
    #     context = {}
    #     data_dict = {}

    #     with pytest.raises(toolkit.ValidationError):
    #         like_dataset(context, data_dict)
    #         likes_has_liked_dataset = mock.Mock(return_value=False)
    #         toolkit.get_action = mock.Mock(return_value=likes_has_liked_dataset)

    #         with mock.patch('ckanext.likes.model.LikeDataset') as mock_like_dataset:
    #             like_instance = mock_like_dataset.return_value
    #             like_instance.save.return_value = None

    #             result = like_dataset(context, data_dict)

    #             assert result == 'This user has successfully liked this dataset.'
    #             mock_like_dataset.assert_called_once_with(user_id="a77e505a-19ea-4e14-9681-fbc3ba06183c")
    #             like_instance.save.assert_called_once()
    
# @pytest.mark.usefixtures("with_request_context")
# def test_like_dataset_user_has_liked_dataset():