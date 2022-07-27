from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Favorites
from products.models import Product


@login_required
def fav_view(request):

    fav_items_count = 0
    try:
        all_favs = Favorites.objects.filter(username=request.user.id)[0]
    except IndexError:
        fav_items = None
    else:
        fav_items = all_favs.products.all()
        fav_items_count = all_favs.products.all().count()

    if not fav_items:
        messages.info(request, 'Nothing to see here!')

    template = 'favorites/favorites.html'
    context = {
        'fav_items': fav_items,
        'fav_items_count': fav_items_count,
    }

    return render(request, template, context)
