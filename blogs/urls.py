from django.urls import path
from .views import BlogTemplateView, BlogDetailView

app_name = 'blogs'

urlpatterns = [
    path('', BlogTemplateView.as_view(), name='list'),
    path('detail/<int:pk>', BlogDetailView.as_view(), name='detail')
]