from django.urls import path, include
from .views import (
    Login,
    Permissions,
)

urlpatterns = [
    path('login/', Login.as_view({
        'post': 'authenticate',
    })),
    path('permissions/', Permissions.as_view({
        'get': 'queryset'
    })),
]
