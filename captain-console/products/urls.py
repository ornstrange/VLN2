from django.urls import path
from . import views

urlpatterns = [
    #  path("offers/", views.offers, name="offers"),
    path("games", views.games, name="games"),
    path("consoles", views.consoles, name="consoles"),
    path("<int:id>/", views.product, name="product")
]

