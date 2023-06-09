from django.shortcuts import _get_queryset
from django.db.models.base import Model

def get_object_or_none(klass, *args, **kwargs):
    """ try to return the class instance and
        return None if none existent.
    """
    queryset = _get_queryset(klass)
    try:
        return queryset.get(*args, **kwargs)
    except queryset.model.DoesNotExist:
        return None


class SerializerProperty(object):

    def __init__(self, *args, **kwargs):
        return super(SerializerProperty, self).__init__(*args, **kwargs)

    @property
    def model(self) -> Model:
        return self.serializer_class.Meta.model