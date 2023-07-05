from django.shortcuts import render
from django.views.generic import ListView, TemplateView

# Create your views here.
class HomeListView(TemplateView):
    template_name = 'index.html'