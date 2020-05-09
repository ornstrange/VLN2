from django.db import models
from django.contrib.auth.models import User
from cart.models import Cart

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField()
    searches = models.TextField(null="true")
    active_cart = models.ForeignKey(Cart, on_delete=models.CASCADE)

