from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('home-page/customer/',views.home),
    path('contact/',views.contact),
    path('about/',views.about),
]
