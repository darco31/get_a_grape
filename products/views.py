from django.shortcuts import render
from .models import Product


def all_products(request):
    """
    View returns the all products page with searching and sorting products
    """

    products = Product.objects.all()

    context = {
        'products': products,
    }

    return render(request, 'products/products.html', context)
