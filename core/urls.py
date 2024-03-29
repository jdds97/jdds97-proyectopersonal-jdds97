"""Core URLs module."""
from django.urls import path
from .views import welcome

urlpatterns = [
    path("welcome/", welcome, name="core_welcome"),
]
