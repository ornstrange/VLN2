from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name="cart"),
    path('checkout/', views.checkout, name="checkout"),
    path('add/', views.add, name="add")
]

