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

import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit
import ckanext.likes.cli as cli
from ckanext.likes.model import setup
from ckanext.likes import actions
from ckanext.likes import auth
from ckanext.likes import helpers
from ckan.lib.plugins import DefaultTranslation
from .cli import init_db

class LikesPlugin(plugins.SingletonPlugin, DefaultTranslation):
    plugins.implements(plugins.IConfigurer)
    plugins.implements(plugins.IConfigurable)
    plugins.implements(plugins.IActions)
    plugins.implements(plugins.IAuthFunctions)
    plugins.implements(plugins.ITemplateHelpers)
    plugins.implements(plugins.ITranslation)
    plugins.implements(plugins.IClick)


    # IConfigurer

    def update_config(self, config_):
        toolkit.add_template_directory(config_, 'templates')
        toolkit.add_public_directory(config_, 'public')
        toolkit.add_resource('fanstatic', 'likes')
    
    # IConfigurable

    def get_commands(self):
        return cli.get_commands()

    def configure(self, config):
         setup()
         #init_db()
         pass

    # IActions

    def get_actions(self):
        return {
            'likes_like_dataset': actions.like_dataset,
            'likes_has_liked_dataset': actions.has_liked_dataset,
            'likes_dislike_dataset': actions.dislike_dataset,
            'likes_dataset_likes_counter': actions.dataset_likes_counter,
            'likes_like_resource': actions.like_resource,
            'likes_has_liked_resource': actions.has_liked_resource,
            'likes_dislike_resource': actions.dislike_resource,
            'likes_resource_likes_counter': actions.resource_likes_counter,
            'likes_like_request': actions.likes_request_like,
            'likes_dislike_request': actions.requests_dislike_request,
            'likes_request_get_likes_count': actions.likes_request_get_likes_count,

        }

    # IAuthFunctions

    def get_auth_functions(self):
        return {
            'likes_like_dataset': auth.like_dataset,
            'likes_has_liked_dataset': auth.has_liked_dataset,
            'likes_dislike_dataset': auth.dislike_dataset,
            'likes_dataset_likes_counter': auth.dataset_likes_counter,
            'likes_like_resource': auth.like_resource,
            'likes_has_liked_resource': auth.has_liked_resource,
            'likes_dislike_resource': auth.dislike_resource,
            'likes_resource_likes_counter': auth.resource_likes_counter,
            'likes_request_like': auth.request_like,
            'likes_request_dislike': auth.request_dislike,
        }

    # ITemplateHelpers

    def get_helpers(self):
        return {
            'likes_has_liked_dataset': helpers.has_liked_dataset,
            'likes_dataset_likes_counter': helpers.dataset_likes_counter,
            'likes_has_liked_resource': helpers.has_liked_resource,
            'likes_resource_likes_counter': helpers.resource_likes_counter,
            'likes_add_requests_likes': helpers.add_requests_likes
        }

    
