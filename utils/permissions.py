from django.shortcuts import _get_queryset
from django.core.exceptions import PermissionDenied

from rest_framework import serializers
from .query import get_object_or_none


def get_user_or_denied(klass, *args, **kwargs):
    """ exception wrapper that will raise
        forbidden restriction if the u
    """
    queryset = _get_queryset(klass)
    try:
        return queryset.get(*args, **kwargs)
    except queryset.model.DoesNotExist:
        raise PermissionDenied()


class RBACPermissionHelper(object):
    """ class that contains RBAC helper methods
    """
    @property
    def model(self):
        return self.Meta.model

    def get_permissions(self, user, model):
        """ return all the user's permission to a
            specific model.
        """
        def __exec():
            for perm in user.roles.filter():
                yield perm.get_permission(model)

        return list(__exec())

    def get_permission_attr(self, user, model, field_name):

        permission = self.get_permissions(user, model)[0]

        def __exec():
            for perm in self.get_permissions(user, model):
                yield perm.role_permission_attrs.get(field_name=field_name)

        return list(set(i for i in __exec()))


class RBACExtendedRestrictionSerializer(RBACPermissionHelper):
    """ helper class to handle updating child
        instances.
    """
    def __save_except(self, value):
        try:
            return value.save() or value
        except AttributeError:
            return value

    def get_model(self, key):
        """ get the model based on the fk object
        """
        return getattr(self.instance, key)._meta.model

    def get_serializer_class_(self, model_name):
        from companies.serializers import CompanySerializer
        return dict((
            ('company', CompanySerializer),
        )).get(model_name)

    def get_childinstance(self, field_name, data):
        """ check if the user action is to reassign the
            instance or just edit a value based on the
            provided data.
        """
        instance = get_object_or_none(
            self.get_model(field_name), id=data.get('id'))

        return instance or getattr(self.instance, field_name)

    def _to_instance(self, field_name, value):
        """ convert FK `id`s to instances
        """
        # check if the key-value set is an FK of the
        # instance
        if type(value) == int and \
            type(getattr(self.instance, field_name)) != int:
            return get_object_or_none(self.get_model(field_name), id=value)
        return value
        
    def to_internal_value(self, data):
        # filter all nested datasets and validate them based on
        # RBAC extended permission from parent permission.
        for key, value in data.items():
            if type(value) == dict:
                # validate if the data are correct or allowed
                # based on their permission.
                serializer = self.get_serializer_class_(key)(
                    data=value,
                    instance=self.get_childinstance(key, value),
                    partial=True,
                    auth_user=self.auth_user,
                    rbac_permission=self.get_permission_attr(self.auth_user, self.model, key),
                )
                serializer.is_valid(raise_exception=True)
                data[key] = serializer

            if type(value) == int:
                data[key] = self._to_instance(key, value)

        return data

    def update(self, instance, data):
        """ update the data
        """
        for field_name, value in data.items():
            data[field_name] = self.__save_except(value)

        instance = super().update(instance, data)
        return instance


class RBACRestrictedSerializer(RBACPermissionHelper):
    """ serializer validator to check for user's access
        to the fields based on the granted permission
    """
    def __init__(self, *args, **kwargs):
        # authenticated user that contains the certain
        # list of RBAC permissions.
        self.auth_user = kwargs.pop('auth_user', None)
        # rbac_permission used for child instance validation
        self.rbac_permission = kwargs.pop('rbac_permission', None)

        return super().__init__(*args, **kwargs)

    def validate(self, data):
        """ validate each field and check if the auth_user
            has been granted access to.
        """
        if not self.auth_user:
            raise AttributeError(f"AttributeError: `request.user` has "
                f"not been passed to the serializer.")

        # validate the user's permission to each field.
        self.rbac_validate(
            data,
            self.rbac_permission or self.get_permissions(self.auth_user, self.model)
        )

        return super().validate(data)

    def rbac_validate(self, data, user_permissions):
        """ validate the data fields based on the
            user's permission
        """
        for field in data.keys():
            for perm in user_permissions:
                if not field in perm.editable_fields():
                    # TODO: map out the error field so it is easier
                    # in the front end to place the error message to the
                    # correct location.
                    raise serializers.ValidationError({
                        field: "*You don't have the right permission on changing this field."
                    })

        return data