"""Imports for home and faqs urls"""
from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='home'),
    path('faqs/', views.faqs, name='faqs'),
    path('shipping/', views.shipping, name='shipping'),
    path('about/', views.about, name='about'),
    path('policy/', views.policy, name='policy'),
    path('contact/', views.contact, name='contact'),
]

handler403 = 'home.views.error_403'
handler404 = 'home.views.error_404'
handler500 = 'home.views.error_500'
