""" Favourites Views """
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.urls import reverse
from products.models import Product
from .models import Favourites


def error_403_view(request, exception):
    '''403 error view'''
    return render(request, '403.html', status=403)


@login_required
def favourites_view(request):
    """
    A view that displays users favourites
    """
    favourite_items_count = 0

    try:
        all_favourites = Favourites.objects.filter(username=request.user.id)[0]
    except IndexError:
        favourite_items = None
    else:
        favourite_items = all_favourites.products.all()
        favourite_items_count = all_favourites.products.all().count()

    if not favourite_items:
        messages.info(request, 'Your favourites list is empty!')

    template = 'favourites/favourites.html'
    context = {
        'favourite_items': favourite_items,
        'favourite_items_count': favourite_items_count
    }

    return render(request, template, context)


@login_required
def add_favourites(request, item_id):
    """
    A view that will add a product item to favourites
    """
    product = get_object_or_404(Product, pk=item_id)
    try:
        favourites = get_object_or_404(Favourites, username=request.user.id)
    except Http404:
        favourites = Favourites.objects.create(username=request.user)

    if product in favourites.products.all():
        messages.info(request, 'The product is already in your favourites!')
    else:
        favourites.products.add(product)
        messages.info(request, 'Added the product to your favourites')

    return redirect(reverse('product_detail', args=[product.id]))


@login_required
def remove_favourites(request, item_id, redirect_from):
    """
    A view that will add a product item to favourites
    """
    product = get_object_or_404(Product, pk=item_id)
    favourites = get_object_or_404(Favourites, username=request.user.id)
    if product in favourites.products.all():
        favourites.products.remove(product)
        messages.success(request, f'{product.name} successfully removed \
            from favourites!')
    else:
        messages.error(request, f'{product.name} is not in your favourites!')

    if redirect_from == 'favourites':
        redirect_url = reverse('favourites')
    else:
        redirect_url = reverse('product_details', args=[product.id])

    return redirect(redirect_url)
