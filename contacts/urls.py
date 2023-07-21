from django.urls import path
from .views import ContactTemplateView, CreateContactView

app_name = 'contacts'

urlpatterns = [
    path('', ContactTemplateView.as_view(), name='page'),
    path('create_contanct/', CreateContactView.as_view(), name='create_contanct')
]