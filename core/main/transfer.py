from django.contrib.auth.decorators import login_required
from django.contrib import messages
from account.models import Account
from django.shortcuts import render, redirect
from account.models import KYC, Account
from account.forms import KYCForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q


@login_required
def searchAccount(request):
    # account = Account.objects.filter(account_status="active")
    account = Account.objects.all()
    # <input name="account_number" placeholder="Search By Account Number
    # or ID" type="text" />
    query = request.POST.get("account_number")
    if query:
        query = query.strip()  # Remove leading/trailing whitespace
        if query:  # Check if query is not empty after stripping
            account = account.filter(
                Q(account_number__iexact=query) |
                Q(account_id__iexact=query)
            ).distinct()
    context = {
        "account": account,
        "query": query,
    }
    return render(request, "transfer/search_account.html", context)


"""
{{account.user.kyc.full_name}}
account is the passed context that will be used in the html page then you can use it.

-------------------------------------------------------------------------------------

<a class="active" href="{%url 'main:transfer-amount' account_number%}">
path("transfer-amount/<account_number>/",transferAmount, name="transfer-amount"),
when you are trying to pass an id of some thing in the html page it should be like 
the above

-------------------------------------------------------------------------------------

"""


def transferAmount(request, account_number):
    # taking the account number of the model == the account number passed in the method
    try:
        account = Account.objects.get(account_number=account_number)
    except:
        # meaning that the account is not passedi in the url
        messages.warning(request, "Account Does Not Exist")
        return redirect("main:search-account")

    context = {
        "account": account,
    }
    return render(request, "transfer/transfer_amount.html", context)
