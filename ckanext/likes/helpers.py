"""likes custom helpers.
"""
from ckan.common import c
from ckan.plugins import toolkit

def has_liked_dataset(dataset_id):
    return toolkit.get_action('likes_has_liked_dataset')({'auth_user_obj': c.userobj}, {'dataset_id': dataset_id})
    
def dataset_likes_counter(dataset_id):
    return toolkit.get_action('likes_dataset_likes_counter')({}, {'dataset_id': dataset_id})