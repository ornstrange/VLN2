from django.shortcuts import render

# Create your views here.

def terms(request):
    return render(request, 'terms/terms.html')