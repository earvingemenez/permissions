from django.contrib import admin

from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .models import (
    Role,
    RolePermission,
    RolePermissionAttribute,
)

@admin.register(get_user_model())
class UserAdmin(BaseUserAdmin):

    readonly_fields = ('date_joined',)
    ordering = ('email',)

    filter_horizontal = ('roles',)
    list_display = ('email', 'first_name', 'last_name', 'date_joined')

    fieldsets = (
        ("Account", {
            'fields': ('email', 'password',),
        }),
        ("Basic Information", {
            'fields': ('first_name', 'last_name', 'roles')
        }),
        ("Others", {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'date_joined')
        })
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2'),
        }),
    )


@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    """ role admin
    """
    list_display = ('name', 'description', 'date_created', 'date_updated')


class RolePermissionAttributeInline(admin.StackedInline):
    """ role permission attr
    """
    model = RolePermissionAttribute
    extra = 0


@admin.register(RolePermission)
class RolePermissionAdmin(admin.ModelAdmin):
    """ role permission admin
    """
    list_display = ('model', 'role', 'can_add',
        'can_edit', 'can_delete', 'can_view')
    inlines = (RolePermissionAttributeInline,)


@admin.register(RolePermissionAttribute)
class RolePermissionAttributeAdmin(admin.ModelAdmin):
    """ role permission attr admin
    """
    list_display = ('role_permission', 'field_name', 'parent', 'model')
    inlines = (RolePermissionAttributeInline,)


# unregister the built-in models from the admin panel
from rest_framework.authtoken.models import TokenProxy
from django.contrib.auth.models import Group

admin.site.unregister(TokenProxy)
admin.site.unregister(Group)