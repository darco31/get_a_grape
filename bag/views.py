from django.shortcuts import render


def view_shopping_bag(request):

    """
    A view to return the bag page
    """

    return render(request, 'bag/bag.html')
