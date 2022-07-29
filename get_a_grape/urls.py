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


handler403 = 'home.views.error_403_view'
handler404 = 'home.views.error_404_view'
handler500 = 'home.views.error_500_view'
handler403 = 'bag.views.error_403_view'
handler404 = 'bag.views.error_404_view'
handler500 = 'bag.views.error_500_view'
handler403 = 'checkout.views.error_403_view'
handler404 = 'checkout.views.error_404_view'
handler500 = 'checkout.views.error_500_view'
handler403 = 'products.views.error_403_view'
handler404 = 'products.views.error_404_view'
handler500 = 'products.views.error_500_view'
handler403 = 'profiles.views.error_403_view'
handler404 = 'profiles.views.error_404_view'
handler500 = 'profiles.views.error_500_view'
handler403 = 'favourite.views.error_403_view'
handler404 = 'favourite.views.error_404_view'
handler500 = 'favourite.views.error_500_view'
