def navigation_links(request):
    return {'navbar_links': [{
        "Home": "index",
        "Offers": "offers",
        "Games": "games",
        "Consoles": "consoles"
    },{
        "About": "about",
        "Cart": "cart",
        "Login": "login"
    }]}
