from django.db import models
from django.utils.translation import gettext as _
from django.utils import timezone
from django.contrib.auth.models import User

from colorfield.fields import ColorField

# Create your models here.


class CategoryModel(models.Model):
    title = models.CharField(max_length=64, verbose_name=_('title'))

    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created at'))

    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')

class BrandModel(models.Model):
    title = models.CharField(max_length=64, verbose_name=_('title'))

    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created at'))

    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name = _('Brand')
        verbose_name_plural = _('Brands')


class SizeModel(models.Model):
    title = models.CharField(max_length=64, verbose_name=_('title'))

    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created at'))

    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name = _('Size')
        verbose_name_plural = _('Sizes')


class ColorModel(models.Model):
    title = models.CharField(max_length=64, verbose_name=_('title'))
    color = ColorField(default='#FF0000')

    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created at'))

    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name = _('Color')
        verbose_name_plural = _('Colors')


class ProductModel(models.Model):
    title = models.CharField(max_length=64, verbose_name=_('product title'))
    image = models.ImageField(upload_to='products', verbose_name=_('image'))
    rating = models.PositiveIntegerField(default=0, verbose_name=_('rating'))
    price = models.DecimalField(max_digits=6, decimal_places=2)
    description = models.TextField(verbose_name=_('description'))
    categories = models.ManyToManyField(CategoryModel, related_name='products')
    brand = models.ForeignKey(BrandModel, on_delete=models.CASCADE, verbose_name=_('brand'), null=True)
    sizes = models.ManyToManyField(SizeModel)
    colors = models.ManyToManyField(ColorModel)

    updated_at = models.DateTimeField(auto_now=True, verbose_name=_('updated at'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created at'))

    def __str__(self) -> str:
        return self.title
    
    def is_new(self):
        now = timezone.now()
        diff = now - self.created_at
        return diff.days <= 3
    
    class Meta:
        verbose_name = _('Product')
        verbose_name_plural = _('Products')
    


class ProductWishlistModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(ProductModel, on_delete=models.SET_NULL, null=True)

    class Meta:
        unique_together = ['user', 'product']
        verbose_name = "Wishlist"
        verbose_name_plural = "Wishlists"