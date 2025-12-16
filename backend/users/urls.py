from .views import role_redirect
from django.urls import path

urlpatterns = [
    path('redirect/', role_redirect, name='role-redirect'),
]