from django.http import HttpResponse
from django.shortcuts import redirect, render
from .forms import *
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages # For Admin Page 
from .models import User

def registerView(request):
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
        form = RegisterForm()
    context = {
        "form": form
    }

    return render(request, "users/register.html", context)


def loginView(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")

        try:
            # Getting user object from the database by email
            user = User.objects.get(email=email)

            # Authenticate it 
            user = authenticate(request,email=email,password=password)
            
            if user is not None:
                # if there is a user and it's already registered then loged him in
                login(request,user)
                messages.success(request, "You are logged.")
                return redirect("main:main")

            else:
                messages.error(request,"User Not Found Try Again")
                return redirect("users:register")
        except:
            messages.error(request,"User Not Found Try ")

    if request.user.is_authenticated:
        messages.warning(request, "You are already logged In")
        return redirect("main:main")
        # return the login page
    return render(request,"users/login.html")

def logoutView(request):
    logout(request)
    messages.success(request,"Successfully loged out.")
    return redirect("users:login")