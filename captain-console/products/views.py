from django.core.paginator import Paginator
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
    paginated_prods = Paginator(prods, 21)
    page_num = request.GET.get('page')
    paged_prods = paginated_prods.get_page(page_num)
    context = {
        'products': paged_prods
    }
    return render(request, 'products/index.html', context)

def product(request, id):
    prod = models.Product.objects.get(pk=id)
    context = {
        'prod': prod
    }
    return render(request, 'products/product.html', context)

