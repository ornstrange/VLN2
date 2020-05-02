from django.shortcuts import render

def index(request):
    return render(request, 'about/index.html')

def employees(request):
    return render(request, 'about/employees.html')

def contact(request):
    return render(request, 'about/contact.html')

