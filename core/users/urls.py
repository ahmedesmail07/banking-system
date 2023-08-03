from django.urls import path 
from .views import *

app_name = "users"

urlpatterns = [
    path("register/", registerView, name="register"),
    path("login/", loginView, name="login"),
    path("logout/", logoutView, name="logout"),

]