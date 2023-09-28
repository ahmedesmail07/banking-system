from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.forms import ValidationError
from account.models import Account
from django.shortcuts import render, redirect
from django.db.models import Q
from django.core.exceptions import ObjectDoesNotExist
from .models import Transactions


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
                Q(account_number__iexact=query) | Q(account_id__iexact=query)
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
    except ValueError:
        # meaning that the account is not passed in the url
        messages.warning(request, "Account Does Not Exist")
        return redirect("main:search-account")

    context = {
        "account": account,
    }
    return render(request, "transfer/transfer_amount.html", context)


def transferAmountProcess(request, account_number):
    # the account that will recieve the amount of the money.
    account = Account.objects.get(account_number=account_number)
    # the logged in user that will send the money
    sender = request.user
    # get the reciever account
    reciever = account.user
    sender_account = sender.account
    reciever_account = account

    if request.method == "POST":
        amount = request.POST.get("send_amount")
        description = request.POST.get("description")

        if sender_account.account_balance > 0 and amount:
            new_transaction = Transactions.objects.create(
                user=request.user,
                amount=amount,
                description=description,
                reciever=reciever,
                sender=sender,
                sender_account=sender_account,
                reciever_account=reciever_account,
                transaction_status="processing",
                transaction_type="transfer",
            )
            new_transaction.save()
            transaction_id = new_transaction.transaction_id
            return redirect(
                "main:transfer-confirmation", account.account_number, transaction_id
            )
        else:
            messages.warning(request, "Insuffient Fund.")
            return redirect("main:transfer-amount", account.account_number)

    else:
        messages.warning(request, "Try Again")
        return redirect("account:account")


def transferConfirmation(request, account_number, transaction_id):
    try:
        account = Account.objects.get(account_number=account_number)
        transaction = Transactions.objects.get(transaction_id=transaction_id)
    except ObjectDoesNotExist:
        raise ValidationError(
            f"There is no transactions of the {transaction_id} or the account number {account_number} is not exist "
        )

    context = {
        "account": account,
        "transaction": transaction,
    }
    return render(request, "transfer/transaction-confirm.html", context)
