from django.shortcuts import get_object_or_404

from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from utils.query import SerializerProperty
from .serializers import (
    VendorSerializer,
    VendorTypeSerializer,
)

from users.permissions import RBACPermission


class Vendors(SerializerProperty, GenericViewSet):
    """ vendors endpoint
    """
    serializer_class = VendorSerializer
    permission_classes = (RBACPermission,)

    def queryset(self, request):
        serializer = self.serializer_class(
            self.model.objects.filter(
                **request.query_params.dict()),
            many=True
        )
        return Response(serializer.data, status=200)


class Vendor(SerializerProperty, GenericViewSet):
    """ vendor endpoint
    """
    serializer_class = VendorSerializer
    permission_classes = (RBACPermission,)

    def get(self, request, **kwargs):
        serializer = self.serializer_class(
            get_object_or_404(self.model, **kwargs)
        )
        return Response(serializer.data, status=200)

    def update(self, request, **kwargs):
        serializer = self.serializer_class(
            data=request.data,
            instance=get_object_or_404(self.model, **kwargs),
            auth_user=request.user,
            #partial=True
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=201)

    def delete(self, request, **kwargs):
        get_object_or_404(self.model, **kwargs).delete()
        return Response(status=204)

    
class VendorTypes(SerializerProperty, GenericViewSet):
    """ vendor type endpoint
    """
    serializer_class = VendorTypeSerializer

    def get(self, request, **kwargs):
        serializer = self.serializer_class(
            self.model.objects.filter(),
            many=True
        )
        return Response(serializer.data, status=200)