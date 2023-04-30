from django.shortcuts import get_object_or_404

from rest_framework import serializers
from rest_framework.serializers import Serializer, ModelSerializer

from companies.serializers import CompanySerializer
from utils.permissions import RBACRestrictedSerializer, RBACExtendedRestrictionSerializer
from .models import Vendor, VendorType


class VendorTypeSerializer(ModelSerializer):
    """ vendor_type serializer
    """
    class Meta:
        model = VendorType
        fields = (
            'id',
            'name',
        )


class VendorSerializer(RBACExtendedRestrictionSerializer,
    RBACRestrictedSerializer, ModelSerializer):
    """ vendor serializer
    """
    company = CompanySerializer()

    class Meta:
        model = Vendor
        fields = (
            'id',
            'company',
            'vendor_type',
            'name',
        )

    def to_representation(self, instance):
        """ customize payload formatting
        """
        resp = super().to_representation(instance)
        resp.update({
            'company': CompanySerializer(instance.company).data,
            'vendor_type': VendorTypeSerializer(instance.vendor_type).data,
        })

        return resp

    # def to_internal_value(self, data):
    #     # validate the child instance `company`
    #     # raise an error if `id` is missing as it is
    #     # not allowed to create a new instance for this model.
    #     company = data.get('company')
    #     if not company.get('id'):
    #         raise serializers.ValidationError({
    #             'id': 'this field is required.'
    #         })

    #     x = CompanySerializer(data=company, partial=True,
    #         auth_user=self.auth_user, rbac_extended=True)
    #     x.is_valid(raise_exception=True)

    #     # vendor_type
    #     data['vendor_type'] = get_object_or_404(VendorType, id=data['vendor_type'])

    #     return data

    # def update(self, instance, data):
    #     import pdb;pdb.set_trace()
    #     # cluster the data sets by popping the
    #     # child data.
    #     # company_data = data.pop('company', None)
    #     # company = CompanySerializer(data=company_data, partial=True, rbac=False)
    #     # company.is_valid(raise_exception=True)
    #     # company.save()

    #     # update the `main instance` first then followed by
    #     # the child instances
    #     instance = super(VendorSerializer, self).update(instance, data)

    #     return instance
