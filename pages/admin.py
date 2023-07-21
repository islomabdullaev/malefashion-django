from django.contrib import admin

from pages.models import BannerCollectionModel, BannerModel

# Register your models here.

admin.site.register(BannerCollectionModel)
@admin.register(BannerModel)
class BannerModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_at', 'updated_at', 'is_active']
    list_editable = ['is_active']