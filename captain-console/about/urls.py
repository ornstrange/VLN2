from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name="about"),
    path('employees', views.employees, name="employees"),
    path('contact', views.contact, name="contact"),
    path('terms', views.terms, name="terms"),
]

