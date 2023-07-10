from django.db import models
from django.utils.translation import gettext as _

# Create your models here.

class AuthorModel(models.Model):
    full_name = models.CharField(max_length=64)
    avatar = models.ImageField(upload_to='avatar')

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = _("Author")
        verbose_name_plural = _("Authors")


class TagModel(models.Model):
    title = models.CharField(max_length=64, verbose_name=_("title"))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _("Tag")
        verbose_name_plural = _("Tags")


class PostModel(models.Model):
    title = models.CharField(max_length=64, verbose_name=_("title"))
    image = models.ImageField(upload_to='image', verbose_name=_("image"))
    banner = models.ImageField(upload_to='banner', verbose_name=_("banner"))
    author = models.ForeignKey(AuthorModel, on_delete=models.CASCADE, verbose_name=_("author"))
    description = models.TextField(verbose_name=_("description"))
    tags = models.ManyToManyField(TagModel, verbose_name=_("tags"))

    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("created at"))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _("Post")
        verbose_name_plural = _("Posts")