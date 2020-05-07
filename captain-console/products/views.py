from django.contrib.postgres.search import SearchVector, SearchQuery
from django.core.paginator import Paginator
from django.shortcuts import render
from . import models

def search(objects, search_term, search_in):
    search_query = SearchQuery(search_term, search_type='phrase')
    search_vector = SearchVector(*search_in)
    return objects.annotate(search=search_vector).filter(search=search_query)

def valid_per_page(per_page_param):
    if per_page_param:
        if per_page_param.isnumeric():
            if 1 < int(per_page_param) <= 64:
                return int(per_page_param)
    return 16

def consoles(request):
    prods = models.Product.objects.filter(category="Console")
    return products(request, prods)

def games(request):
    prods = models.Product.objects.filter(category="Game")
    return products(request, prods)

def products(request, prods=None):
    # all products
    if not prods:
        prods = models.Product.objects.all()
    # search
    if search_term := request.GET.get('search'):
        prods = search(prods, search_term, ('name', 'description',
                                            'keywords', 'condition'))
    # sort
    if (sort_key := request.GET.get('sort')) in ['name', 'price', '-price']:
        prods = prods.order_by(sort_key)
    # products per page
    per_page = valid_per_page(request.GET.get('per_page'))
    # paginate
    paginated_prods = Paginator(prods, per_page - 1)
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

