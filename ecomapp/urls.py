# this is app urls

from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('', views.index, name='comapphome'),
    path('about/',views.about,name='aboutus'),
    path('contact/',views.contact,name='contactus'),
    path('tracker/',views.tracker,name='tracker'),
    path('search/',views.search,name='search'),
    path('products/<int:myid>', views.productview, name='productview'),
    path('checkout/',views.checkout,name='checkout')
]