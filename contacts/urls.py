from django.urls import path
from .views import ContactTemplateView

app_name = 'contacts'

urlpatterns = [
    path('', ContactTemplateView.as_view(), name='page')
]