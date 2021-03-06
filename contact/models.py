"""
Imports
"""
from django.db import models


class Contact(models.Model):
    """
    Contact page model
    """
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=30, blank=True)
    message = models.TextField()
    message_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.name)
