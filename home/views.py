"""Imports for home views and faqs"""
from django.shortcuts import render
from django.core.mail import send_mail
from django.contrib import messages


def error_403(request, exception):
    """
    403 error view
    """
    return render(request, '403.html', status=403)


def error_404(request, exception):
    """
    404 error view
    """
    return render(request, '404.html', status=404)


def error_500(request):
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


def contact(request):
    """View to return contact us page"""

    if request.method == 'POST':
        # Send contact form to Gmail Account
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        message_data = {
            'name': name,
            'email': email,
            'subject': subject,
            'message': message,
        }
        message = '''
        From: {}
        New message: {}
        '''.format(message_data['email'], message_data['message'])

        send_mail(
            message_data['subject'], message, '', ['sdarcy29@gmail.com'])

        messages.info(request, (
            f'Your message has been sent, we will contact you \
                via { email } as soon as possible.'))
        return render(request, 'home/index.html')

    return render(request, 'home/contact.html')