from django.db import models
from django.utils.translation import gettext as _

# Create your models here.

class ContactModel(models.Model):
    name = models.CharField(max_length=64, verbose_name=_('name'))
    email = models.EmailField(max_length=128, verbose_name=_('email'))
    message = models.TextField(verbose_name=_('message'))

    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = _('Contact')
        verbose_name_plural = _('Contacts')

    def __str__(self) -> str:
        return f"{self.email}: {self.message}"