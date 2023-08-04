from django import template

from products.models import ProductWishlistModel

register = template.Library()


@register.filter(name="in_wishlist")
def in_wishlist(product, user):
   return ProductWishlistModel.objects.filter(user=user, product=product).exists()