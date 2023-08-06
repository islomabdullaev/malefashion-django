from django.urls import path
from .views import signin, signout, signup

app_name = 'users'


urlpatterns = [
    path('', signin, name='signin'),
    path('signout/', signout, name='signout'),
    path('signup/', signup, name='signup')
]