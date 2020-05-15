from django.shortcuts import render, redirect
from django.contrib import messages
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

def handler404(request, *args, **argv):
    messages.error(request, 'The page you were looking does not exist.')
    return redirect('home')

def handler500(request, *args, **argv):
    messages.error(request, "Something bad happened, we are very sorry.")
    return redirect('home')

