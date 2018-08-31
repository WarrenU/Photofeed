from django.utils import six


def get_updated_obj(data, obj):
    """
    Returns an object with updated field attributes given from the data param.
    """
    for attr, val in six.iteritems(data):
        setattr(obj, attr, val)
    return obj