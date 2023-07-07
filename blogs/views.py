# Create your views here.
from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.

class BlogTemplateView(TemplateView):
    template_name = 'blog.html'