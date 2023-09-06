from django.db import models
from account.models import Account
from users.models import User
from shortuuid.django_fields import ShortUUIDField

TRANSACTION_TYPE = (
    ("transfered", "Transfered"),
    ("recived", "Recived"),
    ("withdraw", "Withdraw"),
    ("refund", "Refund"),
    ("request", "Request"),
    ("none", "None"),
)

TRANSACTION_STATUS = (
    ("failed", "Failed"),
    ("completed", "Completed"),
    ("pending", "Pending"),
    ("processing", "Processing"),
)


class Transactions(models.Model):
    transaction_id = ShortUUIDField(unique=True, length=15, max_length=20, prefix="TRN")
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, related_name="user"
    )
    amount = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)
    description = models.CharField(max_length=250, null=True, blank=True)
    reciever = models.ForeignKey(
        User, on_delete=models.SET_NULL, related_name="reciever", null=True
    )
    sender = models.ForeignKey(
        User, on_delete=models.SET_NULL, related_name="sender", null=True
    )
    reciever_account = models.ForeignKey(
        Account, on_delete=models.SET_NULL, related_name="reciever_account", null=True
    )
    sender_account = models.ForeignKey(
        Account, on_delete=models.SET_NULL, related_name="sender_account", null=True
    )
    transaction_status = models.CharField(
        choices=TRANSACTION_STATUS, max_length=100, default="Pending"
    )
    transaction_type = models.CharField(
        choices=TRANSACTION_TYPE, max_length=100, default=None
    )
    date = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=False, null=True, blank=True)

    def __str__(self):
        try:
            return f"{self.user}"
        except User.DoesNotExist:
            return "User not found"
        except Exception as e:
            return f"An unexpected error occurred: {str(e)}"
