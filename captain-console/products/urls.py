from django.urls import path
from . import views

urlpatterns = [
    path("offers/", views.offers, name="Offers"),
    path("consoles/", views.consoles, name="Consoles"),
    path("games/", views.games, name="Games"),
]

