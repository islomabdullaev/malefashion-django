from django.urls import path
from .views import BlogTemplateView, BlogDetailView, create_post_comment

app_name = 'blogs'

urlpatterns = [
    path('', BlogTemplateView.as_view(), name='list'),
    path('detail/<int:pk>', BlogDetailView.as_view(), name='detail'),
    path('post/<int:pk>/comment', create_post_comment, name='post_comment' )
]