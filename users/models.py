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

    def get_permission(self, model):
        """ return the list of permission from
            the specified model
        """
        x = ContentType.objects.get_for_model(model)

        return get_user_or_denied(
            apps.get_model('users.Access'), model=x, user=self)


class AccessField(models.Model):
    """ user permission per field/data
    """
    access = models.ForeignKey('users.Access',
        related_name="fields", on_delete=models.CASCADE)
    
    name = models.CharField(max_length=30)
    can_view = models.BooleanField(default=True)
    can_change = models.BooleanField(default=True)

    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name}"


class Access(models.Model):
    """ user permission
    """
    user = models.ForeignKey(get_user_model(),
        related_name="permissions", on_delete=models.CASCADE)
    model = models.ForeignKey(ContentType, on_delete=models.CASCADE)

    can_add = models.BooleanField(default=True)
    can_delete = models.BooleanField(default=True)
    can_view = models.BooleanField(default=True)

    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Access"

    def __str__(self):
        return f"({self.user}) {self.model}"

    @property
    def module(self):
        return f"{self.model.model_class()._meta.verbose_name}"

    @property
    def safe_methods(self):
        """ return the list of safe request methods
            based on the user's permission configuration
        """
        _SAFE_METHODS = ('POST', 'DELETE', 'GET')

        def __validate():
            for i, perm in enumerate([self.can_add, self.can_delete, self.can_view]):
                if perm: yield _SAFE_METHODS[i]

        return list(__validate())

    def changeable_fields(self):
        """ return fields that can be changed by
            the user based on the granted access
        """
        return list(i.name for i in self.fields.filter(can_change=True))


@receiver(post_save, sender=Access)
def after_save(instance=None, created=False, **kwargs):
    """ signal after the instance is save
    """
    if created:
        # generate the access fields based on
        # the model fields.
        for name in get_fields(instance.model.model_class()):
            AccessField.objects.create(access=instance, name=name)

