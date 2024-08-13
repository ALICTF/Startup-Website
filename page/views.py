from django.shortcuts import render
from django.contrib.auth import get_user_model

from .models import Portfolio



def index(request):
    teams = get_user_model().objects.filter(is_staff=False, is_superuser=False, is_active=True)[:4]
    return render(request, 'page/index.html', {'teams': teams})


def portfolio(request):
    portfolios = Portfolio.objects.all()
    
    return render(request, 'page/portfolio.html', {'portfolios': portfolios})


def services(request):
    
    return render(request, 'page/services.html')


def contact(request):
    
    return render(request, 'page/contact.html')
