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


def add_requests_likes(requests, user=None):
    try:
        requests_ids = []
        for req in requests:
            if req.get('id'):
                requests_ids.append(req['id'])
        likes = toolkit.get_action('likes_request_get_likes_count')({
            'user_id': user,
        }, {'requests': requests_ids})
        
        for req in requests:
            if not req.get('id'):
                continue
            likes_info = likes.get(req['id'], {
                'likes': 0,
                'user_liked': False
            })
            req['likes'] = {
                'likes_count': likes_info['likes'],
                'has_liked': likes_info['user_liked']
            }
        return requests
    except:
        import traceback
        traceback.print_exc()
    
    return requests