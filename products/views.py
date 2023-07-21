from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.

class ProductListView(TemplateView):
    template_name = 'shop.html'
