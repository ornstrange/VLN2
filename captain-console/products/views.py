from django.shortcuts import render
from django.http import HttpResponse

def offers(request):
    context = {
        'title': 'Offers',
        'data': ["offer 1", "offer 2"]
    }
    return render(request, 'products/index.html', context)

def consoles(request):
    context = {
        'title': 'Consoles',
        'data': ["console 1", "console 2"]
    }
    return render(request, 'products/index.html', context)

def games(request):
    context = {
        'title': 'Games',
        'data': ["game 1", "game 2"]
    }
    return render(request, 'products/index.html', context)

