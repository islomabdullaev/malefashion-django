from typing import Any, Dict
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import TemplateView, ListView
from django.contrib.auth.models import User

from products.models import CategoryModel, ColorModel, ProductModel, BrandModel, ProductWishlistModel, SizeModel
# Create your views here.


class ProductListView(ListView):
    template_name = 'shop.html'
    model = ProductModel

    def get_context_data(self, **kwargs: Any):
        context = super().get_context_data(**kwargs)
        context['products'] = ProductModel.objects.all().order_by('-created_at')
        context['categories'] = CategoryModel.objects.all()
        context['brands'] = BrandModel.objects.all()
        context['sizes'] = SizeModel.objects.all()
        context['colors'] = ColorModel.objects.all()
        return context


def create_or_delete_wishlist(request, user_pk, product_pk):
    try:
        user = get_object_or_404(User, pk=user_pk)
        product = get_object_or_404(ProductModel, pk=product_pk)
        ProductWishlistModel.objects.create(user=user, product=product)
        return redirect('products:list')
    except:
        ProductWishlistModel.objects.get(user=user, product=product).delete()
        return redirect('products:list')