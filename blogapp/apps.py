"""App configuration for the app"""
from django.apps import AppConfig


class BlogappConfig(AppConfig):
    """Setting auto field to BigAutoField"""

    default_auto_field = "django.db.models.BigAutoField"
    name = "blogapp"
