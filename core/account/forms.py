from tkinter.tix import Select
from django import forms
from .models import KYC
from django.forms import ImageField ,FileInput , DateInput

ACCOUNT_STATUS = (
    ("active","Active"),
    ("in-active","In-Active"),
)

MARITAL_STATUS = (
    ("married","Married"),
    ("single","Single"),
    ("other","Other"),
)

GENDER = (
    ("male","Male"),
    ("female","Female"),
)

IDENTITY_TYPE = (
    ("national_id_card","National Id Card"),
    ("passport","Passport"),
)

class DateInput(forms.DateInput):
    input_type = 'date'

class KYCForm(forms.ModelForm):
    identity_image = ImageField(widget=FileInput)
    identity_type = forms.ChoiceField(choices=IDENTITY_TYPE,)
    image = ImageField(widget=FileInput)
    gender = forms.ChoiceField(choices=GENDER,)
    marital_status = forms.ChoiceField(choices=MARITAL_STATUS,)
    signature = ImageField(widget=FileInput)    

    class Meta:
        model = KYC
        fields = ['full_name', 'mobile', 'gender',\
            'marital_status', 'state', 'date_of_birth','identity_type',\
            'signature','city','country','identity_image','image']  
         
        widgets = {
            "full_name": forms.TextInput(attrs={"placeholder":"full_name"}),
            "mobile": forms.TextInput(attrs={"placeholder":"mobile"}),
            "gender": forms.TextInput(attrs={"placeholder":"gender"}),
            "identity_type": forms.TextInput(attrs={"placeholder":"identity_type"}),
            "marital_status": forms.TextInput(attrs={"placeholder":"marital_status"}),
            "country": forms.TextInput(attrs={"placeholder":"country"}),
            "state": forms.TextInput(attrs={"placeholder":"state"}),
            "date_of_birth": DateInput(attrs={"placeholder":"date"}),
        }