"""
Imports for the favs app
"""
from django.db import models
from django.contrib.auth.models import User
from products.models import Product


class Favourites(models.Model):

    class Meta:
        verbose_name_plural = 'Favourites'

    products = models.ManyToManyField(Product, blank=True)
    username = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.username}'s favourite wines"