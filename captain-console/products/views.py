from django.contrib.postgres.search import SearchVector, SearchQuery
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
    if search_term := request.POST.get('search'):
        print(search_term)
        search_query = SearchQuery(search_term, search_type='phrase')
        prods = prods.annotate(
            search=SearchVector('name', 'description', 'keywords', 'condition'))\
            .filter(search=search_query))
    if sort_key := request.GET.get('sort'):
        prods = prods.order_by(sort_key)
    paginated_prods = Paginator(prods, 22)
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

