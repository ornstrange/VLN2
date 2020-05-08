from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.about, name="about"),
    path('employees', views.employees, name="employees"),
    path('contacts', views.contacts, name="contacts"),
    path('terms', views.terms, name="terms"),
    path('socialresponsibility', views.social, name="social"),
    path('shipping&returns', views.shipping, name="shipping"),

]

