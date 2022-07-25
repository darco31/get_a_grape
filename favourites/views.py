"""
fav app views imports
"""
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.http import Http404
from products.models import Product
from .models import Favourites


@login_required
def favourites_view(request):

    favourite_items_count = 0

    try:
        all_favourites = Favourites.objects.filter(username=request.user.id)[0]
    except IndexError:
        favourite_items = None
    else:
        favourite_items = all_favourites.products.all()
        favourite_items_count = all_favourites.products.all().count()

    if not favourite_items:
        messages.info(request, "Your favourites list is empty")

    template = 'favourites/favourites.html'
    context = {
        'favourite_items': favourite_items,
        'favourite_items_count': favourite_items_count
    }

    return render(request, template, context)
