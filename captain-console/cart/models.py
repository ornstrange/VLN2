from django.db import models
from django.db.models import Sum
from django.dispatch import receiver
from django.db.models.signals import post_delete
from django_countries.fields import CountryField
from products.models import Product
from user.models import User

class Cart(models.Model):
    user = models.ForeignKey(User,
                             null=True,
                             on_delete=models.SET_NULL)
    status = models.CharField(max_length=32)
    created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.id}: {self.status}, {self.user}'s cart."

    @property
    def total_price(self):
        items = Cart_item.objects.filter(cart=self)
        return sum([i.total_price for i in items]) if items else 0

    def contains(self, product):
        all_items = Cart_item.objects.filter(cart=self)
        if all_items.filter(product=product):
            return all_items.get(product=product)
        else:
            return None

    @property
    def all_items(self):
        return Cart_item.objects.filter(cart=self)

class Cart_item(models.Model):
    product = models.ForeignKey(Product,
                                null=True,
                                on_delete=models.SET_NULL)
    quantity = models.IntegerField(default=1)
    cart = models.ForeignKey('Cart',
                             on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.id}: {self.quantity} x {self.product.name}"

    @property
    def total_price(self):
        return self.quantity * self.product.price

@receiver(post_delete, sender='cart.Cart_item')
def delete_if_last(sender, instance, **kwargs):
    cart = instance.cart
    cart_items = Cart_item.objects.filter(cart=cart)
    if len(cart_items) == 0:
        cart.delete()

class Contact_info(models.Model):
    last_name = models.CharField(max_length=64)
    first_name = models.CharField(max_length=64)
    country = CountryField()
    address = models.CharField(max_length=128)
    city = models.CharField(max_length=128)
    postcode = models.CharField(max_length=10)

    def __str__(self):
        return ", ".join([self.last_name, self.first_name,
                          self.country.name, self.address,
                          self.city, self.postcode])

    @property
    def pretty_values(self):
        return {
            'Full name': f"{self.first_name} {self.last_name}",
            'Country': self.country.name,
            'Address': f"{self.postcode}, {self.city}, {self.address}"
        }

class Payment_info(models.Model):
    last_four = models.CharField(max_length=4)
    expiration = models.DateField()
    cardholder = models.CharField(max_length=128)

    def __str__(self):
        return ", ".join([self.cardholder,
                          self.expiration.strftime('%m/%y'),
                          self.last_four])

    @property
    def pretty_values(self):
        return {
            'Cardholder': self.cardholder,
            'Expiration Date': self.expiration.strftime('%m/%y'),
            'Card Number': f"**** **** **** {self.last_four}"
        }

class Order(models.Model):
    user = models.ForeignKey(User,
                             null=True,
                             on_delete=models.SET_NULL)
    cart = models.ForeignKey('Cart',
                             null=True,
                             on_delete=models.SET_NULL)
    contact = models.ForeignKey('Contact_info',
                                null=True,
                                on_delete=models.SET_NULL)
    payment = models.ForeignKey('Payment_info',
                                null=True,
                                on_delete=models.SET_NULL)
    status = models.CharField(max_length=32)
    created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.id}, {self.status}: {self.user}, cart: {self.cart.id}"

