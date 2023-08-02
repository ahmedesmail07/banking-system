from django.urls import path
from .views import *

app_name = "main"

urlpatterns = [
    path("",index,name="main"),
    path("contact/",contact,name="contact"),
    path("about/",about,name="about"),
]