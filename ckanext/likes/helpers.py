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