from django.urls import path
from .views import *
from .transfer import *
app_name = "main"

urlpatterns = [
    path("", index, name="main"),
    path("contact/", contact, name="contact"),
    path("about/", about, name="about"),
    path("search-account/", searchAccount, name="search-account"),
    path("transfer-amount/<account_number>/",
         transferAmount, name="transfer-amount"),

]
