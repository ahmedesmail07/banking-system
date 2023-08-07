from django import forms
from .models import KYC
from django.forms import ImageField ,FileInput , DateInput
from django_countries.fields import CountryField

MARITAL_STATUS = (
    ("married","Married"),
    ("single","Single"),
    ("other","Other"),
)

GENDER = (
    ("male","Male"),
    ("female","Female"),
)

class DateInput(forms.DateInput):
    input_type = 'date'

class KYCForm(forms.ModelForm):
    identity_image = ImageField(widget=FileInput)
    image = ImageField(widget=FileInput)
    gender = forms.ChoiceField(choices=GENDER)
    marital_status = forms.ChoiceField(choices=MARITAL_STATUS)
    country = CountryField()

    class Meta:
        model = KYC
        fields = ['full_name', 'mobile', 'gender', 'marital_status', 'country', 'state', 'city']   
        widgets = {
            "full_name": forms.TextInput(attrs={"placeholder":"full_name"}),
            "mobile": forms.TextInput(attrs={"placeholder":"mobile"}),
            "gender": forms.TextInput(attrs={"placeholder":"gender"}),
            "marital_status": forms.TextInput(attrs={"placeholder":"marital_status"}),
            "country": forms.TextInput(attrs={"placeholder":"country"}),
            "state": forms.TextInput(attrs={"placeholder":"state"}),
            "city": forms.TextInput(attrs={"placeholder":"city"}),
        }