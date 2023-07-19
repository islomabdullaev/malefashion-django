from django.contrib import admin

from contacts.models import ContactModel

# Register your models here.
@admin.register(ContactModel)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'message']