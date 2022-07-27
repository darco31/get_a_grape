from django.urls import path
from . import views

urlpatterns = [
    path('', views.fav_view, name='fav_view')
]
