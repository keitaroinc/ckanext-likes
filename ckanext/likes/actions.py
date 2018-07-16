from ckan.plugins import toolkit
from ckanext.likes.model import LikeDataset
from ckanext.likes.model import LikeResource


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
