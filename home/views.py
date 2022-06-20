from django.shortcuts import render


def index(request):
    """
    View returns the index page
    """
    return render(request, 'home/index.html')
