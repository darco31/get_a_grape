"""
Imports
"""
from django.contrib import admin
from.models import Product, Category


class ProductAdmin(admin.ModelAdmin):
    """
    List display order for products in admin panel
    """
    list_display = (
        'name',
        'category',
        'price',
        'rating',
        'image',
    )

    ordering = ('name',)


class CategoryAdmin(admin.ModelAdmin):
    """
    List display order for categories in admin panel
    """
    list_display = (
        'friendly_name',
        'name',
    )


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
