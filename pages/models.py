from django.db import models
from django.utils.translation import gettext as _

# Create your models here.

class BannerCollectionModel(models.Model):
    title = models.CharField(max_length=64, verbose_name=_('title'))

    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created at'))

    def __str__(self):
        return self.title

class BannerModel(models.Model):
    collection = models.ForeignKey(
        BannerCollectionModel, on_delete=models.CASCADE,
        verbose_name=_('collection'))
    title = models.CharField(max_length=64, verbose_name=_('title'))
    description = models.TextField(verbose_name=_('description'))
    is_active = models.BooleanField(default=False)
    banner = models.ImageField(upload_to='banners', verbose_name=_('banner'))

    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created at'))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_('updated at'))
    def __str__(self) -> str:
        return f"{self.title} --> {self.collection.title}"