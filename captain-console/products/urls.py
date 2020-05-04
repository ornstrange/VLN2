from django.urls import path
from . import views

urlpatterns = [
    path("offers/", views.offers, name="offers"),
    path("consoles/", views.consoles, name="consoles"),
    path("games/", views.games, name="games"),
    path("<int:id>/", views.product, name="product")
]

