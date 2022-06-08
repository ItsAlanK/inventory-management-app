from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('add-product', views.add_product, name='add_product'),
    path('add-location', views.add_location, name='add_location'),
]