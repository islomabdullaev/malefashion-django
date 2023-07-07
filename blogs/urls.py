from django.urls import path
from .views import BlogTemplateView

app_name = 'blogs'

urlpatterns = [
    path('', BlogTemplateView.as_view(), name='list')
]