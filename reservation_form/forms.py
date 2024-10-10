from django import forms
from weapons.models import Weapon
from reservation_form.models import BookedDate
from datetime import datetime, timedelta


class ReservationForm(forms.Form):
    def __init__(self, *args, **kwargs):

        free_dates = kwargs.pop("free_dates", {})
        super().__init__(*args, **kwargs)

        self.fields["date_dropdown"] = forms.ChoiceField(       
            choices = [(date, date) for date in free_dates.keys()],
            label="",
            widget = forms.Select(
                attrs={"class":"form-control", "title":"Choose day"})
            )
    
        self.fields["time_dropdown"] = forms.ChoiceField(
            choices = [],
            label="",
            widget = forms.Select(
                attrs={"class":"form-control", "title":"Choose time for shooting"})
            )

        weapon_data = Weapon.objects.all()
        weapon_choices = [("", "Select a weapon (optional)")] + [(f"{weapon.manufacturer} {weapon.model}", f"{weapon.manufacturer} {weapon.model}") for weapon in weapon_data]

        self.fields["weapon"] = forms.ChoiceField(
            choices = weapon_choices, required = False, label = "",
            widget = forms.Select(
                attrs={"class":"form-control", "title":"In case You want to rent a weapon"})
            )
        self.fields["instructor"] = forms.BooleanField(
            required=False,
            label="If You need an Instructor:",
            widget=forms.CheckboxInput(attrs={"class": "custom-checkbox mr-2"})
            )
        self.fields["name"] = forms.CharField(
            max_length=100, label="", required=True, error_messages = {"required" : "Please enter Your name."},
            widget=forms.TextInput(
                attrs={"class":"form-control", "placeholder":"Name", "title":"Enter Your name"})
            )
        self.fields["email"] = forms.EmailField(
            label="", required=True, error_messages = {"required" : "Please enter Your email."},
            widget=forms.TextInput(
                attrs={"class":"form-control", "placeholder":"Email", "title":"Enter Your email"})
            )

    class Meta:
        model = Weapon
        fields = ["model", "weapon_types"]

    