from django.shortcuts import _get_queryset
from django.core.exceptions import PermissionDenied

from rest_framework import serializers


def get_user_or_denied(klass, *args, **kwargs):
    """ exception wrapper that will raise
        forbidden restriction if the u
    """
    queryset = _get_queryset(klass)
    try:
        return queryset.get(*args, **kwargs)
    except queryset.model.DoesNotExist:
        raise PermissionDenied()


class AUTHUSERException(object):
    """ Exception class that checks if the `auth_user` which
        contains the request.user object was passed to the
        parent class.
    """
    def __init__(self, *args, **kwargs):
        self.auth_user = kwargs.pop('auth_user', None)
        if not self.auth_user:
            raise AttributeError("AttributeError: `request.user` has not been passed to the serializer.")
        return super().__init__(*args, **kwargs)


class RBACRestrictedSerializer(AUTHUSERException):
    """ serializer validator to check for user's access
        to the fields based on the granted permission
    """
    @property
    def model(self):
        return self.Meta.model

    def validate(self, data):
        """ validate each field and check if the auth_user
            has been granted access to.
        """
        permission = self.auth_user.get_permission(self.model)

        for field in data.keys():
            if not field in permission.changeable_fields():
                raise serializers.ValidationError({
                    field: "*You don't have the right access on changing this field."
                })

        return super().validate(data)
