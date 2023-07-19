from django.http import HttpResponse
from django.views.generic import TemplateView, CreateView
from contacts.models import ContactModel
# Create your views here.

class ContactTemplateView(TemplateView):
    template_name = 'contact.html'


def create_contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")
        
        contanct = ContactModel(name=name, email=email, message=message)
        contanct.save()
        
        return HttpResponse('Created')