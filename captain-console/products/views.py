from django.contrib.postgres.search import SearchVector, SearchQuery
from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.contrib import messages
from user.models import Search
from products.models import Product

def search(products, search_term, search_in):
    search_query = SearchQuery(search_term, search_type='phrase')
    search_vector = SearchVector(*search_in)
    return products.annotate(search=search_vector).filter(search=search_query)

def valid_per_page(per_page_param):
    if per_page_param:
        if per_page_param.isnumeric():
            if 1 < int(per_page_param) <= 64:
                return int(per_page_param)
    return 16

def find_keyword_opts(products):
    skip = ['Game', 'Console']
    keywords = {}
    for product in products:
        for keyword in product.keywords.split(', '):
            if keyword not in skip:
                if keyword in keywords:
                    keywords[keyword] += 1
                else:
                    keywords[keyword] = 1
    sorted_keys = sorted(keywords.keys(),
                         key=lambda x: keywords[x],
                         reverse=True)
    output = []
    for key in sorted_keys:
        outstr = f"{key} / {keywords[key]} result"
        outstr += "s" if keywords[key] > 1 else ""
        output.append((key, outstr))
    return output

def consoles(request):
    prods = Product.objects.filter(category="Console")
    return products(request, prods)

def games(request):
    prods = Product.objects.filter(category="Game")
    return products(request, prods)

def new_search(user, prods, search_term):
    if len(prods) > 0 and user.is_authenticated:
        if not user.customer.last_search:
            return Search(user=user.customer,
                          search_term=search_term)
        elif user.customer.last_search.search_term != search_term:
            return Search(user=user.customer,
                          search_term=search_term)
    return False

def products(request, prods=None):
    # all products
    if not prods:
        prods = Product.objects.all()
    # search
    if search_term := request.GET.get('search'):
        prods = search(prods, search_term, ('name', 'description',
                                            'keywords', 'condition'))
        # add Search object to user if relevant
        if search_obj := new_search(request.user, prods, search_term):
            request.user.customer.last_search = search_obj
            search_obj.save()
            request.user.save()
    # keywords
    keyword_opts = find_keyword_opts(prods)
    active_filter = None
    if keyword := request.GET.get('keyword'):
        if keyword != 'reset':
            active_filter = keyword
            prods = prods.filter(keywords__icontains=keyword)
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
        'products': paged_prods,
        'keyword_opts': keyword_opts,
        'active_filter': active_filter,
        'per_page': per_page,
        'script': 'products.js',
        'style': 'products.css'
    }
    return render(request, 'products/index.html', context)

def product(request, id):
    if request.method == "POST":
        messages.error(request, "You have to be logged in to add to your cart.")
        return redirect('login')
    prod = Product.objects.get(pk=id)
    prev = request.META.get('HTTP_REFERER')
    if prod.get_absolute_url() in prev:
        prev = '/products/'
        prev += 'games' if prod.category == "Game" else 'consoles'
    print(prev)
    context = {
        'prod': prod,
        'prev': prev,
        'style': 'products.css'
    }
    return render(request, 'products/product.html', context)

