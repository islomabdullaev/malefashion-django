# Create your views here.
from typing import Any
from django.db import models
from django.db.models.query import QuerySet
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse, reverse_lazy
from django.views.generic import TemplateView, ListView, DetailView
from blogs.forms import CommentForm

from blogs.models import PostModel
# Create your views here.

class BlogTemplateView(ListView):
    template_name = 'blog.html'
    model = PostModel

    def get_queryset(self):
        queryset = PostModel.objects.all()
        tag = self.request.GET.get('tag')
        if tag:
            queryset = PostModel.objects.filter(tags__title=tag)

        return queryset


class BlogDetailView(DetailView):
    template_name = 'blog-details.html'
    model = PostModel
    context_object_name = 'post'


def create_post_comment(request, pk):
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            post = get_object_or_404(PostModel, pk=pk)
            form = form.save(commit=False)
            form.post = post
            form.save()

            return redirect(reverse('blogs:detail', kwargs={"pk":pk}))
        else:
            return HttpResponse('Please enter a valid data')