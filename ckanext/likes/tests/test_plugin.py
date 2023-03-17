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

import ckanext.likes.plugin as plugin
from unittest import TestCase
from unittest.mock import patch
from ckanext.likes.actions import like_dataset, has_liked_dataset
from ckanext.likes.model import LikeDataset, LikeResource, LikeRequests

# def test_plugin():
#     pass

class TestLikes(TestCase):
    
    def setUp(self):
        context={"auth_user_obj":{"id":"a77e505a-19ea-4e14-9681-fbc3ba06183c"}}
        data_dict={"dataset_id":"a599491d-f12e-4761-92b3-b0868fb421a4"}
            
    # @patch()
