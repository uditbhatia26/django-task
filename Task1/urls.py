from django.contrib import admin
from django.urls import path
from Task1 import views

urlpatterns = [
    path("join", views.join, name='join'),
    path("", views.join, name='home'),
    path("show", views.show, name="show")
]

