"""Imports for home and faqs urls"""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('faqs/', views.faqs, name='faqs'),
    path('shipping/', views.shipping, name='shipping'),
]