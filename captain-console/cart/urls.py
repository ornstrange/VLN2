from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='cart'),
    path('add/', views.add, name='add_item'),
    path('del/', views.delete, name='delete_item'),
    path('add_q/', views.add_quantity, name='add_quantity'),
    path('dec_q/', views.dec_quantity, name='dec_quantity'),
    path('checkout/', views.checkout, name='checkout'),
    path('checkout/payment', views.checkout_payment, name='checkout_payment'),
    path('checkout/review', views.checkout_review, name='checkout_review'),
    path('checkout/confirm', views.checkout_confirm, name='checkout_confirm')
]

