from django.urls import path
from .views import AboutUsView, HomeListView

app_name = 'pages'

urlpatterns = [
    path('', HomeListView.as_view(), name='home'),
    path('about-us/', AboutUsView.as_view(), name='about')
]