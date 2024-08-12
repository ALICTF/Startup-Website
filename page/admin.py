from django.contrib import admin

from .models import Portfolio

@admin.register(Portfolio)
class Portfolio(admin.ModelAdmin):
    list_display = ['name']
    list_per_page = 20
