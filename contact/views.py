from django.shortcuts import render,redirect
from django.core.mail import EmailMessage
from django.contrib import messages
from contact.forms import ContactForm

def leave_message(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():

            name = form.cleaned_data["name"]
            email = form.cleaned_data["email"]
            message = form.cleaned_data["message"]

            EmailMessage(
                f"Web message from {name}",
                f"Text: {message}, contact: {email}",
                "HlavackaDanielml@seznam.cz",
                ["HlavackaDanielml@seznam.cz"],
                [],
            ).send()

            EmailMessage(
                "Web message",
                "Thank You for Your message! Someone will contact You ASAP. :-)",
                "HlavackaDanielml@seznam.cz",
                [email],
                [],
            ).send()

            messages.success(request, "Your message is in our hands.")
            return redirect("leave_message")
    else:
        form = ContactForm()

    return render(request, "contact/contact.html", {"form":form, "messages": messages.get_messages(request)})
                       