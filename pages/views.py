from typing import Any, Dict
from django.shortcuts import render
from django.views.generic import ListView, TemplateView

# Create your views here.
class HomeListView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs: Any):
        context = super().get_context_data(**kwargs)
        context['posts'] = 
        return context