"""likes custom helpers.
"""
from ckan.common import c
from ckan.plugins import toolkit

def has_liked_dataset(dataset_id):
    return toolkit.get_action('likes_has_liked_dataset')({'auth_user_obj': c.userobj}, {'dataset_id': dataset_id})
    
def dataset_likes_counter(dataset_id):
    return toolkit.get_action('likes_dataset_likes_counter')({}, {'dataset_id': dataset_id})

def has_liked_resource(resource_id):
    return toolkit.get_action('likes_has_liked_resource')({'auth_user_obj': c.userobj}, {'resource_id': resource_id})

def resource_likes_counter(resource_id):
    return toolkit.get_action('likes_resource_likes_counter')({}, {'resource_id': resource_id})