from django.urls import path
from .views import Companies, Company, CompanyTypes

urlpatterns = [
    path('types/', CompanyTypes.as_view({
        'get': 'get',
    })),
    path('', Companies.as_view({
        'get': 'queryset',
        'post': 'create',
    })),
    path('<int:id>/', Company.as_view({
        'get': 'get',
        'put': 'update',
    })),
]