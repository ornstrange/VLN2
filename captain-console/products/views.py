from django.shortcuts import render
from . import models

def consoles(request):
    # search / filter here
    prods = models.Product.objects.filter(category="Console")
    return products(request, prods)

def games(request):
    # search / filter here
    prods = models.Product.objects.filter(category="Game")
    return products(request, prods)

def products(request, prods):
    context = {
        'products': prods[:20]
    }
    return render(request, 'products/index.html', context)

def product(request, id):
    prod = models.Product.objects.get(pk=id)
    context = {
        'prod': prod
    }
    return render(request, 'products/product.html', context)

