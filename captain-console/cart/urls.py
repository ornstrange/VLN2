from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name="cart"),
    path('checkout/', views.checkout, name="checkout"),
    path('add/', views.add, name="add_item"),
    path('del/', views.delete, name="delete_item"),
    path('add_q/', views.add_quantity, name="add_quantity"),
    path('dec_q/', views.dec_quantity, name="dec_quantity")
]

