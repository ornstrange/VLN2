from products.models import Product

def navigation_links(request):
    # links
    left = ['home', 'games', 'consoles']
    center = ['search']
    right = [('Information', ({'About us': 'about'}, 'employees', 'contact'))]
    if request.user.is_authenticated:
        if request.user.customer.last_search:
            sub_menu = ({'Search history': 'search_history'},
                        {'View profile': 'profile'}, 'logout')
        else:
            sub_menu = ({'View profile': 'profile'}, 'logout')
        right += [(request.user, sub_menu), 'cart']
    else:
        right += ['login']
    return {'navbar_links': [left, center, right]}

def names(request):
    name = request.resolver_match.url_name
    if name == "product":
        prod_id = request.resolver_match.kwargs['id']
        name = Product.objects.filter(id=prod_id)[0].name
    return {'name': name, 'title': name.capitalize()}

