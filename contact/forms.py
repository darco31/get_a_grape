"""
Form for contacts
"""

from django.forms import ModelForm
from .models import Contact


class ContactForm(ModelForm):
    """
    Submission forms
    """
    class Meta:
        model = Contact
        fields = [
            'name',
            'email',
            'phone_number',
            'message',
        ]

