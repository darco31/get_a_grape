"""
Imports for apps
"""
from django.apps import AppConfig


class BagConfig(AppConfig):
    """
    Apps config
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'bag'
