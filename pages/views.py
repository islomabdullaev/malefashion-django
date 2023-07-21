from typing import Any, Dict
from django.shortcuts import render
from django.views.generic import ListView, TemplateView
from blogs.models import PostModel

from pages.models import BannerModel

# Create your views here.
class HomeListView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['banners'] = BannerModel.objects.filter(is_active=True)
        context['posts'] = PostModel.objects.order_by('-pk')[:3]
        return context


class AboutUsView(TemplateView):
    template_name = 'about.html'