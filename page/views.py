from django.shortcuts import render

from .models import Portfolio


def index(request):
    
    return render(request, 'page/index.html')


def portfolio(request):
    portfolio = Portfolio.objects.all()
    context = {
        'portfolio': portfolio
    }
    
    return render(request, 'page/portfolio.html', context)


def services(request):
    
    return render(request, 'page/services.html')


def contact(request):
    
    return render(request, 'page/contact.html')
