# captain_console URL Configuration
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views

# Errors
handler404 = 'captain_console.views.handler404'
handler500 = 'captain_console.views.handler500'

# Urls
urlpatterns = [
    path('', views.index, name="home"),
    path('products/', include('products.urls')),
    path('about/', include('about.urls')),
    path('cart/', include('cart.urls')),
    path('admin/', admin.site.urls),
    path('user/', include('user.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

