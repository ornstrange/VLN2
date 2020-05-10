from django.db import models
from django.contrib.auth.models import User
from cart.models import Cart

class Customer(models.Model):
    user = models.OneToOneField(User,
                                on_delete=models.CASCADE)
    name = models.TextField(null=True)
    avatar = models.ImageField()
    last_search = models.ForeignKey(Search,
                                    null=True,
                                    on_delete=models.SET_NULL)
    active_cart = models.ForeignKey(Cart,
                                    null=True,
                                    on_delete=models.SET_NULL)

class Search(models.Model):
    user = models.ForeignKey(Customer,
                             on_delete=models.CASCADE)
    search_term = models.CharField(max_length=256)
    date = models.DateTimeField(auto_now=True)

