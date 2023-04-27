from django.contrib.auth import authenticate, get_user_model

from rest_framework import serializers
from rest_framework.serializers import Serializer, ModelSerializer

from utils.query import get_object_or_none
from .models import Access, AccessField

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


class FieldSerializer(serializers.ModelSerializer):
    """ access field
    """
    class Meta:
        model = AccessField
        fields = ('name', 'can_view', 'can_change')


class PermissionSerializer(serializers.ModelSerializer):
    """ user access
    """
    fields = FieldSerializer(many=True)

    class Meta:
        model = Access
        fields = (
            'id',
            'module',
            'can_add',
            'can_delete',
            'fields',
        )