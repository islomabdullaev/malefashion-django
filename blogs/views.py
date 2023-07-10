# Create your views here.
from django.shortcuts import render
from django.views.generic import TemplateView, ListView

from blogs.models import PostModel
# Create your views here.

class BlogTemplateView(ListView):
    template_name = 'blog.html'
    model = PostModel