from django.conf import settings
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404

from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from rest_framework.permissions import AllowAny, IsAuthenticated

from .serializers import (
    LoginSerializer,
    RoleSerializer,
)


class Login(GenericViewSet):
    """ authentication endpoint
    """
    authentication_class = ()
    permission_classes = (AllowAny,)
    serializer_class = LoginSerializer

    def authenticate(self, request):
        serializer = self.serializer_class(
            data=request.data, request=request)
        serializer.is_valid(raise_exception=True)
        
        return Response(serializer.data, status=200)


class Permissions(GenericViewSet):
    """ user permission/access
    """
    serializer_class = RoleSerializer

    def queryset(self, request):
        serializer = self.serializer_class(
            request.user.roles.filter(), many=True)

        return Response(serializer.data, status=200)