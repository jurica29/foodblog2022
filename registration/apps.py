"""Importing app configuration"""
from django.apps import AppConfig


class RegistrationConfig(AppConfig):
    """Setting default auto fields to bigautofield"""

    default_auto_field = "django.db.models.BigAutoField"
    name = "registration"
