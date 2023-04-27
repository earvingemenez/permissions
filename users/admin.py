from django.contrib import admin

from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .models import Access, AccessField

@admin.register(get_user_model())
class UserAdmin(BaseUserAdmin):

    readonly_fields = ('date_joined',)
    ordering = ('email',)

    filter_horizontal = ('groups', 'user_permissions',)
    list_display = ('email', 'first_name', 'last_name', 'date_joined')

    fieldsets = (
        ("Account", {
            'fields': ('email', 'password',),
        }),
        ("Basic Information", {
            'fields': ('first_name', 'last_name',)
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


class AccessFieldInline(admin.StackedInline):

    model = AccessField
    extra = 0
    readonly_fields = ('name',)


@admin.register(Access)
class AccessAdmin(admin.ModelAdmin):

    list_display = ('user', 'model', 'can_add', 'can_delete', 'date_updated')
    inlines = (AccessFieldInline,)


# unregister the built-in models from the admin panel
from rest_framework.authtoken.models import TokenProxy
from django.contrib.auth.models import Group

admin.site.unregister(TokenProxy)
admin.site.unregister(Group)