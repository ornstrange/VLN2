from django.urls import path
from . import views

urlpatterns = [
    #  path("offers/", views.offers, name="offers"),
    path("", views.terms, name="terms")
]


