from django.urls import path
from .views import Vendors, Vendor, VendorTypes

urlpatterns = [
    path('types/', VendorTypes.as_view({
        'get': 'get',
    })),
    path('', Vendors.as_view({
        'get': 'queryset',
    })),
    path('<int:id>/', Vendor.as_view({
        'get': 'get',
        'put': 'update',
        'delete': 'delete',
    })),
]