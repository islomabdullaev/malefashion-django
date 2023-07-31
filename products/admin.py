from django.contrib import admin

from products.models import CategoryModel, BrandModel, ProductWishlistModel, SizeModel, ColorModel, ProductModel

# Register your models here.

admin.site.register(CategoryModel)
admin.site.register(BrandModel)
admin.site.register(SizeModel)
admin.site.register(ColorModel)
admin.site.register(ProductModel)   
admin.site.register(ProductWishlistModel)