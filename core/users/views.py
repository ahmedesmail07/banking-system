from django.http import HttpResponse
from django.shortcuts import redirect, render
from .forms import *
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages # For Admin Page 


def RegisterView(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            # saving the form data inside the new_user variable
            new_user = form.save()
            # getting whatever passed into the email field
            username = form.cleaned_data.get("username")
            # username = request.POST.get("username") == the above
            messages.success(
                request, f"Hey {username} your account has been created successfully.")
            # Auto log in the user into the website
            new_user = authenticate(username=form.cleaned_data["email"],
                                    password=form.cleaned_data["password1"])
            # new_user = authenticate(username=form.cleaned_data.get("email"))
            login(request, new_user)
            # Redirect to "name of the app : name of the url"
            return redirect("main:main")
    
    if request.user.is_authenticated:
            messages.warning(
                request, f"Hey Method Not Allowed, You are already logged in.")
            return redirect("main:main")
    else:
        form = RegisterForm(request.POST)
    context = {
        "form": form
    }

    return render(request, "users/register.html", context)
