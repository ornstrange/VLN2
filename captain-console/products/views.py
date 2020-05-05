from django.shortcuts import render
from . import models

def products(request, title, objects):
    context = {
        'title': title,
        'products': objects
    }
    return render(request, 'products/index.html', context)

def consoles(request):
    objects = models.Product.objects.filter(category="Console")
    return products(request, 'Console', objects)

def games(request):
    objects = models.Product.objects.filter(category="Game")
    return products(request, 'Games', objects)

def product(request, id):
    prod = models.Product.objects.get(pk=id)
    context = {
        'title': prod.name,
        'prod': prod
    }
    return render(request, 'products/product.html', context)

