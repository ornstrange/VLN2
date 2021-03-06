from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.urls import reverse
from cart.models import Cart

class Customer(models.Model):
    user = models.OneToOneField(User,
                                on_delete=models.CASCADE)
    avatar = models.ImageField(null=True)
    last_search = models.ForeignKey('Search',
                                    null=True,
                                    on_delete=models.SET_NULL)
    active_cart = models.ForeignKey(Cart,
                                  null=True,
                                  on_delete=models.SET_NULL)

    def __str__(self):
        return self.user.username

@receiver(post_save, sender='auth.User')
def create_customer(sender, instance, created, **kwargs):
    if created:
        Customer.objects.create(user=instance)
    else:
        instance.customer.save()

class Search(models.Model):
    user = models.ForeignKey('Customer',
                             on_delete=models.CASCADE)
    search_term = models.CharField(max_length=256)
    date = models.DateTimeField(auto_now=True)

    @property
    def pretty_date(self):
        return self.date.strftime('%d/%m/%y - %H:%M:%S')

    def __str__(self):
        return f"{self.user.user} searched: {self.search_term}"

    def get_absolute_url(self):
        return reverse('search') + f'?search={self.search_term}'

