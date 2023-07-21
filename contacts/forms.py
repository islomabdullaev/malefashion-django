from django import forms

from contacts.models import ContactModel


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactModel
        exclude = ['id', 'created_at', 'updated_at']
