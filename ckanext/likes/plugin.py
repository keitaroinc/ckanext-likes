import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit
from ckanext.likes.model import setup
from ckanext.likes import actions
from ckanext.likes import auth
from ckanext.likes import helpers

class LikesPlugin(plugins.SingletonPlugin):
    plugins.implements(plugins.IConfigurer)
    plugins.implements(plugins.IConfigurable)
    plugins.implements(plugins.IActions)
    plugins.implements(plugins.IAuthFunctions)
    plugins.implements(plugins.ITemplateHelpers)

    # IConfigurer

    def update_config(self, config_):
        toolkit.add_template_directory(config_, 'templates')
        toolkit.add_public_directory(config_, 'public')
        toolkit.add_resource('fanstatic', 'likes')
    
    # IConfigurable

    def configure(self, config): 
        setup()


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

    
