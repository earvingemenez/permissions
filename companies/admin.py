from django.contrib import admin
from .models import Company

@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    """ company admin panel
    """
    list_display = ('name', 'country', 'type', 'status')