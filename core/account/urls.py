from django.urls import path
from .views import *

app_name = "account"

urlpatterns = [
    path("kyc-register/", kycRegisteration, name="kyc-register"),
    path("", accountView, name="account"),


]
