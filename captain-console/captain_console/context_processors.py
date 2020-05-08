from products.models import Product

def navigation_links(request):
    # user logged in
    authenticated = request.user.is_authenticated
    # links
    left = ['home', 'games', 'consoles']
    center = ['#search']
    right = ['about']
    right += ['cart', '#user'] if authenticated else ['login']
    return {'navbar_links': [left, center, right]}

def names(request):
    name = request.resolver_match.url_name
    if name == "product":
        prod_id = request.resolver_match.kwargs['id']
        name = Product.objects.filter(id=prod_id)[0].name
    return {'name': name, 'title': name.capitalize()}

