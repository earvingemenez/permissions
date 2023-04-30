import datetime

from django.apps import apps
from django.conf import settings
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.contrib.auth import get_user_model
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from django.utils import timezone

from rest_framework.authtoken.models import Token
from utils.models import get_fields
from utils.permissions import get_user_or_denied

from .managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    """ user info
    """
    email = models.EmailField(max_length=500, unique=True)
    first_name = models.CharField(max_length=80)
    last_name = models.CharField(max_length=80)

    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    roles = models.ManyToManyField('users.Role', blank=True)

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ("first_name", "last_name")

    def __str__(self):
        return f"{self.email}"

    def get_display_name(self):
        return f"{self.last_name.title()}, {self.first_name.title()}"

    def get_token(self):
        """ get or generate an auth token that is valid
            for `settings.AUTH_TOKEN_EXPIRY_TIME`
        """
        token, created = Token.objects.get_or_create(user=self)
        expiry_date = token.created + datetime.timedelta(
            days=settings.AUTH_TOKEN_EXPIRY_TIME)
        
        if not created and expiry_date < timezone.now():
            token.delete()
            token = Token.objects.create(user=self)
        
        return token


class Role(models.Model):
    """ user role
    """
    name = models.CharField(max_length=100)
    description = models.TextField()

    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name}"

    def get_permission(self, model):
        """ get the user's permission instance
            on a specific model/module
        """
        return get_user_or_denied(
            apps.get_model('users.RolePermission'),
            model=ContentType.objects.get_for_model(model),
            role=self
        )


class RolePermission(models.Model):
    """ role permission
    """
    role = models.ForeignKey('users.Role',
        related_name="role_permissions", on_delete=models.CASCADE)
    model = models.ForeignKey(ContentType, on_delete=models.CASCADE)

    can_add = models.BooleanField(default=True) 
    can_edit = models.BooleanField(default=True)
    can_delete = models.BooleanField(default=True)
    can_view = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.role} | {self.model}"

    @property
    def module(self):
        return f"{self.model.model_class()._meta.verbose_name}"

    @property
    def safe_methods(self):
        """ return the list of safe request methods
            based on the user's permission configuration
        """
        _SAFE_METHODS = ('POST', 'PUT', 'DELETE', 'GET')

        def __validate():
            for i, perm in enumerate([self.can_add,
                self.can_edit, self.can_delete, self.can_view]):
                if perm: yield _SAFE_METHODS[i]
        
        return list(__validate())

    def editable_fields(self):
        """ return fields that can be edited by the
            user based on the granted access
        """
        return list(i.field_name for i in \
            self.role_permission_attrs.filter(can_edit=True))


@receiver(post_save, sender=RolePermission)
def after_save(instance=None, created=False, **kwargs):
    """ signal after the instance is save
    """
    if created:
        # generate the access fields based on
        # the model fields.
        for name in get_fields(instance.model.model_class()):
            apps.get_model('users.RolePermissionAttribute').objects \
                .create(role_permission=instance, field_name=name)


class RolePermissionAttribute(models.Model):
    """ role permission attribute
    """
    parent = models.ForeignKey('self', related_name="child_perm_attrs",
        null=True, blank=True, on_delete=models.SET_NULL)
    model = models.ForeignKey(ContentType, null=True, blank=True, on_delete=models.SET_NULL)
    
    role_permission = models.ForeignKey('users.RolePermission',
        related_name="role_permission_attrs", on_delete=models.CASCADE)
    field_name = models.CharField(max_length=50)

    can_add = models.BooleanField(default=True)
    can_edit = models.BooleanField(default=True)
    can_delete = models.BooleanField(default=True)
    can_view = models.BooleanField(default=True)

    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.field_name}"

    def editable_fields(self):
        """ return the fields that can be edited by user
            based on this child attr.
        """
        return list(i.field_name for i in \
            self.child_perm_attrs.filter(can_edit=True))
