from django.contrib.auth.decorators import login_required
from account.models import Account
from django.shortcuts import render, redirect
from account.models import KYC, Account
from account.forms import KYCForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required


@login_required
def searchAccount(request):
    # account = Account.objects.filter(account_status="active")
    account = Account.objects.all()
    context = {
        "account": account,
    }
    return render(request, "transfer/search_account.html", context)
