from django.http import HttpResponse
from django.urls import reverse
from django.views.generic import TemplateView, CreateView
from contacts.forms import ContactForm
from contacts.models import ContactModel
# Create your views here.

class ContactTemplateView(TemplateView):
    template_name = 'contact.html'


class CreateContactView(CreateView):
    template_name = 'contact.html'
    form_class = ContactForm

    def get_success_url(self):
        return reverse('contacts:page')