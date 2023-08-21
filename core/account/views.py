import re
from tkinter import NO
from django.shortcuts import redirect, render
from .models import KYC, Account
from .forms import KYCForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required


# @login_required
def accountView(request):
    if request.user.is_authenticated:
        try:
            kyc = KYC.objects.get(user=request.user)
        except:
            messages.warning(request, "You Should Submit your kyc first.")
            return redirect("account:kyc-register")
        account = Account.objects.get(user=request.user)
    else:
        messages.warning(request, "you should login to access the dashboard")
        return redirect("users:login")


@login_required
def kycRegisteration(request):
    user = request.user
    account = Account.objects.get(user=user)

    try:
        kyc = KYC.objects.get(user=user)
    except:
        kyc = None

    context = {
        "account": account,
        "form": None,
        "kyc": kyc
    }

    if request.method == "POST":
        form = KYCForm(request.POST, request.FILES, instance=kyc)
        if form.is_valid():
            new_form = form.save(commit=False)
            new_form.user = user
            new_form.account = account
            new_form.save()
            print(form.errors)
            messages.success(
                request, "KYC Confirmed Successfully, In Review Now")
            return redirect("main:main")
    else:
        form = KYCForm(instance=kyc)

    context["form"] = form
    return render(request, "account/kyc_form.html", context)
