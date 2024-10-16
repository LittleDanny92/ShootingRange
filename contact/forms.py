from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(
        max_length=100, label="", required=True, error_messages = {"required" : "Please enter Your name."},
        widget=forms.TextInput(attrs={"class":"form-control", "placeholder":"Name", "title":"Enter Your name"})
        )
    email = forms.EmailField(
        label="", required=True, error_messages = {"required" : "Please enter Your email."},
        widget=forms.TextInput(attrs={"class":"form-control", "placeholder":"Email", "title":"Enter Your email"})
        )
    message = forms.CharField(
        label="", required=True, error_messages = {"required" : "Please leave the message."},
        widget=forms.Textarea(attrs={"class":"form-control", "rows":5, "placeholder":"Message", "title":"Leave a message"})
        )
