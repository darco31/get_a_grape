""" Imports for URLS main app"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', include('home.urls')),
    path('products/', include('products.urls')),
    path('bag/', include('bag.urls')),
    path('checkout/', include('checkout.urls')),
    path('profile/', include('profiles.urls')),
    path('favourite/', include('favourite.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


handler403 = 'home.views.handle_403'
handler404 = 'home.views.handle_404'
handler500 = 'home.views.handle_500'
handler403 = 'bag.views.handle_403'
handler404 = 'bag.views.handle_404'
handler500 = 'bag.views.handle_500'
handler403 = 'checkout.views.handle_403'
handler404 = 'checkout.views.handle_404'
handler500 = 'checkout.views.handle_500'
handler403 = 'products.views.handle_403'
handler404 = 'products.views.handle_404'
handler500 = 'products.views.handle_500'
handler403 = 'profiles.views.handle_403'
handler404 = 'profiles.views.handle_404'
handler500 = 'profiles.views.handle_500'
handler403 = 'favourites.views.handle_403'
handler404 = 'favourites.views.handle_404'
handler500 = 'favourites.views.handle_500'
