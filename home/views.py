"""Imports for home views and faqs"""
from django.shortcuts import render


def index(request):
    """
    View returns the index page
    """
    return render(request, 'home/index.html')


def faqs(request):
    """
    Returns faq page
    """
    return render(request, 'home/faqs.html')
