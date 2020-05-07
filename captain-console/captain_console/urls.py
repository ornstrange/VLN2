# captain_console URL Configuration
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name="home"),
    path('products/', include('products.urls')),
    path('about/', include('about.urls')),
    path('cart/', include('cart.urls')),
    path('admin/', admin.site.urls),
    path('user/', include('user.urls')),
    path('terms/', include('info_foot.urls'))
]

