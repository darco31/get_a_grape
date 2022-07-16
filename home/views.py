"""Imports for home views and faqs"""
from django.shortcuts import render
from django.core.mail import send_mail
from django.contrib import messages


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


def contact(request):
    """ A view to return the Contact Us page """
    if request.method == "POST":
        message_name = request.POST['message-name']
        message_email = request.POST['emailaddress']
        message = request.POST['message']

        send_mail('message from ' + message_name,
                  message + ' reply to this message ' + message_email,
                  message_email,
                  ['sdarcy29@gmail.com'])
        messages.success(request,
                         'Email received. We will contact you shortly.')
        return render(request, "home/contactus.html")
    else:
        return render(request, "home/contactus.html")
