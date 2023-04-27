from itertools import chain

from django.contrib.contenttypes.models import ContentType
from rest_framework.permissions import BasePermission

class RBACPermission(BasePermission):
    """ access checker based on the user's
        granted permission.
    """
    def has_permission(self, request, view):
        # get the auth user's permission list based on
        # the model data that the user wants to access
        permissions = request.user.permissions.filter(
            model=ContentType.objects.get_for_model(view.model))

        def __perms():
            for perm in permissions:
                yield perm.safe_methods
        
        safe_methods = list(set(i for i in chain.from_iterable(__perms())))
        return request.method in safe_methods
