from django.shortcuts import get_object_or_404

from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from utils.query import SerializerProperty
from .serializers import CompanySerializer

from users.permissions import RBACPermission


class Companies(SerializerProperty, GenericViewSet):
    """ companies endpoint
    """
    serializer_class = CompanySerializer
    permission_classes = (RBACPermission,)

    def queryset(self, request):
        serializer = self.serializer_class(
            self.model.objects.filter(
                **request.query_params.dict()),
            many=True,
            auth_user=request.user
        )
        return Response(serializer.data, status=200)

    def create(self, request):
        serializer = self.serializer_class(
            data=request.data, auth_user=request.user)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=201)


class Company(SerializerProperty, GenericViewSet):
    """ company endpoint
    """
    serializer_class = CompanySerializer
    permission_classes = (RBACPermission,)

    def get(self, request, **kwargs):
        serializer = self.serializer_class(
            get_object_or_404(self.model, **kwargs)
        )
        return Response(serializer.data, status=200)

    def update(self, request, **kwargs):
        serializer = self.serializer_class(
            data=request.data,
            instance=get_object_or_404(self.model, **kwargs)
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=200)

    def delete(self, request, **kwargs):
        get_object_or_404(self.model, **kwargs).delete()
        return Response(status=204)