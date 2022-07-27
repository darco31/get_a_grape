"""
Favs app imports
"""
from django.contrib import admin
from .models import Favorites


class FavAdmin(admin.ModelAdmin):

    list_display = ['username']
    search_fields = ['username']
    list_filter = ['username']


admin.site.register(Favorites, FavAdmin)
