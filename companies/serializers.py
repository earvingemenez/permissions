from rest_framework import serializers
from rest_framework.serializers import Serializer, ModelSerializer

from utils.permissions import RBACRestrictedSerializer
from .models import Company, CompanyType


class CompanyTypeSerializer(ModelSerializer):
    """ company type serializer
    """
    class Meta:
        model = CompanyType
        fields = (
            'id',
            'desc',
        )


class CompanySerializer(RBACRestrictedSerializer, ModelSerializer):
    """ company serializer
    """
    class Meta:
        model = Company
        fields = (
            'id',
            'name',
            'country',
            'company_type',
            'status',
            'date_created',
            'date_updated',
        )

    def to_representation(self, instance):
        resp = super().to_representation(instance)
        # resp.update({
        #     'company_type': CompanyTypeSerializer(instance.company_type).data,
        # })

        return resp
