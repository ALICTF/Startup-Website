from django.urls import path

app_name = 'page'

from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('contact/', views.contact, name='contact'),
    path('portfolio/', views.portfolio, name='portfolio'),
    path('services/', views.services, name='services'),
]