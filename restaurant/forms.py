# dango imports
from django import forms
from django.forms import ModelForm

# local imports
from .models import Booking


# Booking form with custom widgets
class BookingForm(ModelForm):
    no_of_guests = forms.ChoiceField(
        choices=[(i, i) for i in range(1, 7)],
        widget=forms.Select(),
        label="No of guests",
    )

    class Meta:
        model = Booking
        fields = "__all__"
        widgets = {
            "booking_date": forms.DateInput(
                attrs={
                    "type": "date",
                    "placeholder": "dd/mm/yyyy",
                    "class": "form-control",
                }
            ),
            "name": forms.TextInput(attrs={"class": "form-control"}),
            "no_of_guests": forms.Select(attrs={"class": "form-control"}),
        }
