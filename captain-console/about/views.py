from django.shortcuts import render

def about(request):
    context = {
        'style': 'about.css'
    }
    return render(request, 'about/about_us.html', context=context)

def employees(request):
    context = {
        'style': 'about.css'
    }
    return render(request, 'about/employees.html', context=context)

def contacts(request):
    context = {
        'style': 'about.css'
    }
    return render(request, 'about/contact.html', context=context)

def terms(request):
    context = {
        'style': 'about.css'
    }
    return render(request, 'about/terms.html', context=context)

def social(request):
    context = {
        'style': 'about.css'
    }
    return render(request, 'about/social_responsibility.html', context=context)

def shipping(request):
    context = {
        'style': 'about.css'
    }
    return render(request, 'about/shipping_returns.html', context=context)

