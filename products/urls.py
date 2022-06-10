from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('add-product', views.add_product, name='add_product'),
    path('edit/<int:product_id>/', views.edit_product, name='edit_product'),
    path('delete/<int:product_id>/', views.delete_product, name='delete_product'),
    path('add-inventory/<int:product_id>/', views.add_inventory, name='add_inventory'),
    path('add-location', views.add_location, name='add_location'),
    path('locations', views.locations, name='locations'),
    path('edit-location/<int:location_id>/', views.edit_location, name='edit_location'),
]