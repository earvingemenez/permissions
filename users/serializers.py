from django.contrib.auth import authenticate, get_user_model

from rest_framework import serializers
from rest_framework.serializers import Serializer, ModelSerializer

from utils.query import get_object_or_none
from .models import Role, RolePermission, RolePermissionAttribute


class LoginSerializer(Serializer):
    """ authenicate user
    """
    user = None
    error = "Incorrect Credentials. Please try again."

    email = serializers.CharField(write_only=True)
    password = serializers.CharField(write_only=True)

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        return super().__init__(*args, **kwargs)

    def validate(self, data):
        email, password = data.values()

        if not email or not password:
            raise serializers.ValidationError(self.error, code="auth")

        user = get_object_or_none(get_user_model(), email__iexact=email)
        if not user:
            raise serializers.ValidationError(self.error, code="auth")

        self.user = authenticate(request=self.request, **data)
        if not self.user:
            raise serializers.ValidationError(self.error, code="auth")

        return data

    def to_representation(self, instance):
        resp = super().to_representation(instance)
        resp.update({'token': self.user.get_token().key})

        return resp


class PermissionAttributeSerializer(ModelSerializer):
    """ role permission attr
    """
    class Meta:
        model = RolePermissionAttribute
        fields = (
            'id',
            'role_permission',
            'field_name',
            'can_add',
            'can_edit',
            'can_delete',
            'can_view',
        )


class PermissionSerializer(ModelSerializer):
    """ role permission serializer
    """
    role_permission_attrs = PermissionAttributeSerializer(many=True, read_only=True)

    class Meta:
        model = RolePermission
        fields = (
            'id',
            'module',
            'can_add',
            'can_edit',
            'can_delete',
            'can_view',
            'role_permission_attrs',
        )


class RoleSerializer(ModelSerializer):
    """ role serializer
    """
    role_permissions = PermissionSerializer(many=True, read_only=True)

    class Meta:
        model = Role
        fields = (
            'id',
            'name',
            'description',
            'role_permissions',
        )
