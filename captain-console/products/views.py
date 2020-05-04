from django.shortcuts import render
from . import models

def offers(request):
    context = {
        'title': 'Offers',
        'products': models.Product.objects.all()
    }
    return render(request, 'products/index.html', context)

def consoles(request):
    context = {
        'title': 'Consoles',
        'products': models.Product.objects.all()
    }
    return render(request, 'products/index.html', context)

def games(request):
    context = {
        'title': 'Games',
        'products': models.Product.objects.all()
    }
    return render(request, 'products/index.html', context)

def product(request, id):
    if id:
        prod = models.Product.objects.get(pk=id)
        context = {
            'title': prod.name,
            'prod': prod
        }
        return render(request, 'products/product.html', context)
    return None

