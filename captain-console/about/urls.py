from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.about, name="about"),
    path('employees', views.employees, name="employees"),
    path('contact', views.contacts, name="contact"),
    path('terms', views.terms, name="terms"),
    path('social_responsibility', views.social, name="social"),
    path('shipping&returns', views.shipping, name="shipping")
]

