from ckan.plugins import toolkit
from ckanext.likes.model import LikeDataset, LikeRequests, LikeResource, get_request


def like_dataset(context, data_dict):
   
    if data_dict.get('dataset_id') is None:
        raise toolkit.ValidationError({toolkit._('dataset_id'): [toolkit._('Missing value')]})

    toolkit.check_access('likes_like_dataset', context, data_dict) 

    user_id = context.get('auth_user_obj').id

    dataset_id = data_dict.get('dataset_id')

    userHasLikedDataset = toolkit.get_action('likes_has_liked_dataset')(context, {'dataset_id': dataset_id})

    if not userHasLikedDataset:
        likedDataset = LikeDataset(user_id=user_id, dataset_id=dataset_id)
        likedDataset.save()
        return toolkit._('This user has successfully liked this dataset.')
    else:
        return toolkit._('This user has already liked this dataset.')

@toolkit.side_effect_free
def has_liked_dataset(context, data_dict):

    if data_dict.get('dataset_id') is None:
        raise toolkit.ValidationError({toolkit._('dataset_id'): [toolkit._('Missing value')]})

    toolkit.check_access('likes_like_dataset', context, data_dict) 

    user_id = context.get('auth_user_obj').id

    dataset_id = data_dict.get('dataset_id')

    userHasLikedDataset = LikeDataset.get(user_id=user_id, dataset_id=dataset_id)

    if userHasLikedDataset:
        return True
    else:
        return False

def dislike_dataset(context, data_dict):

    if data_dict.get('dataset_id') is None:
       raise toolkit.ValidationError({toolkit._('dataset_id'): [toolkit._('Missing value')]})

    toolkit.check_access('likes_dislike_dataset', context, data_dict)

    user_id = context.get('auth_user_obj').id
    dataset_id = data_dict.get('dataset_id')
    userHasLikedDataset = toolkit.get_action('likes_has_liked_dataset')(context, {'dataset_id': dataset_id})


    if userHasLikedDataset:
        likedDataset = LikeDataset.get(user_id=user_id, dataset_id=dataset_id)
        LikeDataset.delete(likedDataset)
        return toolkit._('This user has successfully disliked this dataset.')
    else:
        return toolkit._('This user has already disliked this dataset.')

@toolkit.side_effect_free
def dataset_likes_counter(context, data_dict):

    if data_dict.get('dataset_id') is None:
       raise toolkit.ValidationError({toolkit._('dataset_id'): [toolkit._('Missing value')]})

    dataset_id = data_dict.get('dataset_id')
    total_likes = LikeDataset.total_likes(dataset_id)
    return int(total_likes)

def like_resource(context, data_dict):
   
    if data_dict.get('resource_id') is None:
        raise toolkit.ValidationError({toolkit._('resource_id'): [toolkit._('Missing value')]})

    toolkit.check_access('likes_like_resource', context, data_dict) 

    user_id = context.get('auth_user_obj').id

    resource_id = data_dict.get('resource_id')

    userHasLikedResource = toolkit.get_action('likes_has_liked_resource')(context, {'resource_id': resource_id})

    if not userHasLikedResource:
        likedResource = LikeResource(user_id=user_id, resource_id=resource_id)
        likedResource.save()
        return toolkit._('This user has successfully liked this resource.')
    else:
        return toolkit._('This user has already liked this resource.')

@toolkit.side_effect_free
def has_liked_resource(context, data_dict):

    if data_dict.get('resource_id') is None:
        raise toolkit.ValidationError({toolkit._('resource_id'): [toolkit._('Missing value')]})

    toolkit.check_access('likes_like_resource', context, data_dict) 

    user_id = context.get('auth_user_obj').id

    resource_id = data_dict.get('resource_id')

    userHasLikedResource = LikeResource.get(user_id=user_id, resource_id=resource_id)

    if userHasLikedResource:
        return True
    else:
        return False

def dislike_resource(context, data_dict):

    if data_dict.get('resource_id') is None:
       raise toolkit.ValidationError({toolkit._('resource_id'): [toolkit._('Missing value')]})

    toolkit.check_access('likes_dislike_resource', context, data_dict)

    user_id = context.get('auth_user_obj').id
    resource_id = data_dict.get('resource_id')
    userHasLikedResource = toolkit.get_action('likes_has_liked_resource')(context, {'resource_id': resource_id})


    if userHasLikedResource:
        likedResource = LikeResource.get(user_id=user_id, resource_id=resource_id)
        LikeResource.delete(likedResource)
        return toolkit._('This user has successfully disliked this resource.')
    else:
        return toolkit._('This user has already disliked this resource.')

@toolkit.side_effect_free
def resource_likes_counter(context, data_dict):

    if data_dict.get('resource_id') is None:
       raise toolkit.ValidationError({toolkit._('resource_id'): [toolkit._('Missing value')]})

    resource_id = data_dict.get('resource_id')
    total_likes = LikeResource.total_likes(resource_id)
    return int(total_likes)


@toolkit.side_effect_free
def likes_request_get_likes_count(context, data_dict):
    if not data_dict.get('requests'):
        return {}
    requests = data_dict['requests']
    likes = LikeRequests.total_likes_for_requests(requests)
    user_likes = {}
    user_id = None
    if context.get('auth_user_obj'):
        user_id = context.get('auth_user_obj').id
    elif context.get('user_id'):
        user_id = context.get('user_id')
    if user_id:
        user_likes = LikeRequests.total_likes_for_requests(requests, user_id=user_id)
    
    result = {}
    for req_id in requests:
        result[req_id] = {
            'likes': likes.get(req_id) or 0,
            'user_liked': True if user_likes.get(req_id) else False
        }
    return result


def likes_request_like(context, data_dict):
    toolkit.check_access('likes_request_like', context, data_dict)

    user_id = context.get('auth_user_obj').id
    request_id = data_dict.get('id')
    if not request_id:
        raise  toolkit.ValidationError({'id': [toolkit._('Missing value')]})
    request = get_request(request_id)
    if not request:
        raise toolkit.NotFound()
    
    request_like = LikeRequests.get(user_id=user_id, request_id=request_id)

    if request_like:
        return toolkit._('This user has already liked this request')
    
    request_like = LikeRequests(user_id=user_id, request_id=request_id)
    request_like.save()

    return toolkit._('This user has successfully liked this request')



def requests_dislike_request(context, data_dict):
    toolkit.check_access('likes_request_dislike', context, data_dict)

    user_id = context.get('auth_user_obj').id
    request_id = data_dict.get('id')
    if not request_id:
        raise  toolkit.ValidationError({'id': [toolkit._('Missing value')]})

    request = get_request(request_id)
    if not request:
        raise toolkit.NotFound()
    
    request_like = LikeRequests.get(user_id=user_id, request_id=request_id)

    if not request_like:
        return toolkit._('This user has not liked this request')
    
    LikeRequests.delete(request_like)

    return toolkit._('This user has successfully disliked this request')