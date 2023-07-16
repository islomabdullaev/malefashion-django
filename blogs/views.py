# Create your views here.
from typing import Any
from django.db import models
from django.shortcuts import get_object_or_404, render
from django.views.generic import TemplateView, ListView, DetailView
from blogs.forms import CommentForm

from blogs.models import PostModel
# Create your views here.

class BlogTemplateView(ListView):
    template_name = 'blog.html'
    model = PostModel


class BlogDetailView(DetailView):
    template_name = 'blog-details.html'
    model = PostModel
    context_object_name = 'post'


def create_post_comment(request, pk):
    if request.method == "POST":
        form = CommentForm(request.POST)
        post = get_object_or_404(PostModel, pk=pk)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            form.save()