from django.shortcuts import render

def about(request):
    return render(request, 'about/about_us.html')

def employees(request):
    return render(request, 'about/employees.html')

def contacts(request):
    return render(request, 'about/contact.html')

def terms(request):
    return render(request, 'about/terms.html')

def social(request):
    return render(request, 'about/social_responsibility.html')

def shipping(request):
    return render(request, 'about/shipping_returns.html')

def employees(request):
    return render(request, 'about/employees.html')

