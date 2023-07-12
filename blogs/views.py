# Create your views here.
from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView

from blogs.models import PostModel
# Create your views here.

class BlogTemplateView(ListView):
    template_name = 'blog.html'
    model = PostModel


class BlogDetailView(DetailView):
    template_name = 'blog-details.html'
    model = PostModel
    context_object_name = 'post'