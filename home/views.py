"""Imports for home views and faqs"""
from django.shortcuts import render


def error_403_view(request, exception):
    """
    403 error view
    """
    return render(request, '403.html', status=403)


def error_404_view(request, exception):
    """
    404 error view
    """
    return render(request, '404.html', status=404)


def error_500_view(request):
    """
    500 error view
    """
    return render(request, '500.html', status=500)


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


def shipping(request):
    """
    Returns shipping page
    """
    return render(request, 'home/shipping.html')


def about(request):
    """
    Returns about page
    """
    return render(request, 'home/about.html')


def policy(request):
    """
    Returns policy page
    """
    return render(request, 'home/policy.html')
