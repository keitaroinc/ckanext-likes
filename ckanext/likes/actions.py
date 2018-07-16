from ckan.plugins import toolkit
from ckanext.likes.model import LikeDataset


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