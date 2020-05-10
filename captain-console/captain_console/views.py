from django.shortcuts import render
from products import models
from datetime import date
import random
from random import choice


def random_items(today):
    items = models.Product.objects.all()
    random.seed(hash(today))
    # change 3 to how many random items you want
    randomitems = random.sample(list(items), 3)
    return randomitems


def index(request):
    today = str(date.today())
    items = random_items(today)
    products = items
    context = {"products":products}
    return render(request, 'index.html', context=context)
