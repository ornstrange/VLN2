from django.shortcuts import render
from products.models import Product
from random import sample, seed
from datetime import date

def daily_random_products(count = 3):
    products = list(Product.objects.all())
    seed(str(date.today()))
    sampled_prods = sample(products, count)
    return sampled_prods

def index(request):
    products = daily_random_products()
    context = {
        'products': products,
        'style': 'products.css'
    }
    return render(request, 'index.html', context=context)

