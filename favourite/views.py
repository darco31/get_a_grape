from django.shortcuts import render


def fav_view(request):

    return render(request, 'fav/fav.html')

