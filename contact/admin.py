"""
Imports for contact admin
"""

from django.contrib import admin
from .models import Contact


class ContactAdmin(admin.ModelAdmin):
    """
    List and filter displays
    for the admin panel
    """
    list_display = ['message_date', 'name', 'id']
    list_filter = ('name', 'message_date')


admin.site.register(Contact, ContactAdmin)
