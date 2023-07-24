from django.shortcuts import render
from django.views.generic import TemplateView, ListView

from products.models import ProductModel
# Create your views here.

class ProductListView(ListView):
    template_name = 'shop.html'
    model = ProductModel
    context_object_name = 'products'