"""
Contact page views
"""
from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from .forms import ContactForm


def contact(request):
    """
    This view shows and submits the query form and shows the success/error
    messages.
    """
    if request.method == 'POST':
        form = ContactForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request,
                             ('Thanks for getting in contact with us,'
                              'We will be in contact as soon as possible.'))

            return redirect(reverse('contact'))
        else:
            messages.error(request,
                           ('Sorry I didnt quite catch that'
                            'Please try again'))

    else:
        form = ContactForm()

    template = 'contacts/contact.html'

    context = {
        'form': form,
        'bag_details_not_required': True
    }

    return render(request, template, context)
