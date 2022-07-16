"""Importing application configuration from apps"""
from django.apps import AppConfig


class BlogConfig(AppConfig):
    """Setting auto field to BigAutoField"""
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'blog'
