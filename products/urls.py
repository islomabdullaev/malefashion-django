from django.urls import path
from .views import ProductListView, create_or_delete_wishlist

app_name = 'products'

urlpatterns = [
    path('', ProductListView.as_view(), name='list'),
    path('wishlist/user/<int:user_pk>/product/<int:product_pk>',
         create_or_delete_wishlist, name="create_wishlist")
]