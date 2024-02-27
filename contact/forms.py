from django import forms
from django.core.validators import EmailValidator

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={"class":"form-control", "placeholder":"Enter name"}), label="")
    email = forms.CharField(validators=[EmailValidator()], widget=forms.TextInput(attrs={"class":"form-control", "placeholder":"Enter email"}), label="")
    message = forms.CharField(widget=forms.Textarea(attrs={"class":"form-control", "rows":5, "placeholder":"Enter the message"}), label="")