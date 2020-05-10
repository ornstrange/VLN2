from django.urls import path
from . import views

urlpatterns = [
    path("search", views.products, name="search"),
    path("games", views.games, name="games"),
    path("consoles", views.consoles, name="consoles"),
    path("<int:id>/", views.product, name="product")
]

