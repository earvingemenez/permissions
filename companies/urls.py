from django.urls import path
from .views import Companies, Company

urlpatterns = [
    path('', Companies.as_view({
        'get': 'queryset',
        'post': 'create',
    })),
    path('<int:id>/', Company.as_view({
        'get': 'get',
        'post': 'update',
    })),
]