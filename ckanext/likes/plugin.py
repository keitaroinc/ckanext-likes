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
            'likes_dataset_likes_counter': actions.dataset_likes_counter
        }

    # IAuthFunctions

    def get_auth_functions(self):
        return {
            'likes_like_dataset': auth.like_dataset,
            'likes_has_liked_dataset': auth.has_liked_dataset,
            'likes_dislike_dataset': auth.dislike_dataset,
            'likes_dataset_likes_counter': auth.dataset_likes_counter
        }

    # ITemplateHelpers

    def get_helpers(self):
        return {
            'likes_has_liked_dataset': helpers.has_liked_dataset,
            'likes_dataset_likes_counter': helpers.dataset_likes_counter
        }

    
