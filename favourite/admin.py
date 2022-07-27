"""
Imports for the favorites app
"""
from django.contrib import admin
from .models import Favourites


class FavsAdmin(admin.ModelAdmin):

    list_display = ['username']


admin.site.register(Favourites, FavsAdmin)