from itertools import chain

from django.contrib.contenttypes.models import ContentType
from rest_framework.permissions import BasePermission

from utils.permissions import RBACPermissionHelper


class RBACPermission(RBACPermissionHelper, BasePermission):
    """ access checker based on the user's
        granted permission.
    """
    def has_permission(self, request, view):
        # get the auth user's roles to get the granted
        # permission for that specific user.
        def __perms():
            for perm in self.get_permissions(request.user, view.model):
                yield perm.safe_methods
        
        safe_methods = list(set(i for i in chain.from_iterable(__perms())))
        return request.method in safe_methods
