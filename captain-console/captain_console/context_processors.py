from products.models import Product

def navigation_links(request):
    user = "login"
    return {'navbar_links': [
        ["home", "games", "consoles"],
        ["about", "cart", user]
    ]}

def names(request):
    name = request.resolver_match.url_name
    if name == "product":
        prod_id = request.resolver_match.kwargs['id']
        name = Product.objects.filter(id=prod_id)[0].name
    return {'title': name.capitalize()}

