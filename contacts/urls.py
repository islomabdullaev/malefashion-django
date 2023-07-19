from django.urls import path
from .views import ContactTemplateView, create_contact

app_name = 'contacts'

urlpatterns = [
    path('', ContactTemplateView.as_view(), name='page'),
    path('create_contanct/', create_contact, name='create_contanct')
]