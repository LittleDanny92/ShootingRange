from django.shortcuts import render
from contact.models import Contact

def get_contact(request):
    contact = Contact.objects.all()
    context = {
        "entire_contact": contact,
    }
    return render(request, "contact/contact.html", context)
