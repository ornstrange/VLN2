def navigation_links(request):
    user = "login"
    return {'navbar_links': [{
        "Home": "home",
        "Games": "games",
        "Consoles": "consoles"
    },{
        "About": "about",
        "Cart": "cart",
        "Login": user
    }]}
