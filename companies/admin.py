from django.contrib import admin
from .models import (
    Company,
    CompanyType,
)


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    """ company admin
    """
    list_display = ('name', 'country', 'company_type', 'status')


@admin.register(CompanyType)
class CompanyTypeAdmin(admin.ModelAdmin):
    """ company type admin
    """
    list_display = ('desc', 'date_created', 'date_updated')
