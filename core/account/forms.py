from django import forms
from numpy import identity
from .models import KYC
from django.forms import ImageField ,FileInput , DateInput

class DateInput(forms.DateInput):
    input_type = 'date'

class KYCForm(forms.ModelForm):
    identity_image = ImageField(widget=FileInput)
    image = ImageField(widget=FileInput)

    class Meta:
        model = KYC
        fields = KYC._meta.fields   
        widget = {
            "full_name": forms.TextInput(attrs={"placeholder":"full_name"}),
            "mobile": forms.TextInput(attrs={"placeholder":"mobile"}),
            "gender": forms.TextInput(attrs={"placeholder":"gender"}),
            "country": forms.TextInput(attrs={"placeholder":"country"}),
            "state": forms.TextInput(attrs={"placeholder":"state"}),
            "city": forms.TextInput(attrs={"placeholder":"city"}),

        }