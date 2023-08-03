from django.urls import path 
from .views import *

app_name = "users"

urlpatterns = [
    path("register/", RegisterView, name="register"),
    path("login/", LoginView, name="login"),
    path("logout/", LogoutView, name="logout"),

]