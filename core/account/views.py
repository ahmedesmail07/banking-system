import re
from tkinter import NO
from django.shortcuts import redirect, render
from .models import KYC, Account
from .forms import KYCForm
from django.contrib import messages

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
    }

    if request.method == "POST":
        form = KYCForm(request.POST, request.FILES, instance=kyc)
        if form.is_valid():
            new_form = form.save(commit=False)
            new_form.user = user
            new_form.account = account
            new_form.save()
            messages.success(request, "KYC Confirmed Successfully, In Review Now")
            return redirect("main:main")
    else:
        form = KYCForm(instance=kyc)

    context["form"] = form
    return render(request, "account/kyc_form.html", context)
