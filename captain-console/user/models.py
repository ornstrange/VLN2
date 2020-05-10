from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from cart.models import Cart

class Customer(models.Model):
    user = models.OneToOneField(User,
                                on_delete=models.CASCADE)
    avatar = models.ImageField()
    last_search = models.ForeignKey('Search',
                                    null=True,
                                    on_delete=models.SET_NULL)
    active_cart = models.ForeignKey(Cart,
                                    null=True,
                                    on_delete=models.SET_NULL)

@receiver(post_save, sender=User)
def create_customer(sender, instance, created, **kwargs):
    if created:
        Customer.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_customer(sender, instance, **kwargs):
    instance.customer.save()

class Search(models.Model):
    user = models.ForeignKey('Customer',
                             on_delete=models.CASCADE)
    search_term = models.CharField(max_length=256)
    date = models.DateTimeField(auto_now=True)

