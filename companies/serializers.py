from rest_framework import serializers
from rest_framework.serializers import Serializer, ModelSerializer

from utils.permissions import RBACRestrictedSerializer
from .models import Company

class CompanySerializer(RBACRestrictedSerializer, ModelSerializer):
    """ company serializer
    """
    class Meta:
        model = Company
        fields = (
            'id',
            'name',
            'country',
            'type',
            'status',
            'date_created',
            'date_updated',
        )