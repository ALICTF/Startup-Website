from django.shortcuts import render

from .models import Portfolio


def index(request):
    
    return render(request, 'page/index.html')


def portfolio(request):
    
    return render(request, 'page/portfolio.html')


def services(request):
    
    return render(request, 'page/services.html')


def contact(request):
    
    return render(request, 'page/contact.html')
