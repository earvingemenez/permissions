from django.contrib import admin
from .models import Vendor, VendorType


@admin.register(Vendor)
class VendorAdmin(admin.ModelAdmin):
    """ vendor admin
    """
    list_display = ('name', 'company', 'vendor_type')


@admin.register(VendorType)
class VendorTypeAdmin(admin.ModelAdmin):
    """ vendor type admin
    """
    list_display = ('name', 'date_created', 'date_updated')
