from django.urls import path
from .views import login, registration

app_name = 'users'

urlpatterns = [
    path('', registration, name='main'),
    path('login/', login, name='login')
]