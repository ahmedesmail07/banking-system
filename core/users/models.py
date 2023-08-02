from django.db import models

from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    username = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    # For Creating Superusers from the website instead of terminal
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    # To Login using EMAIL not the username of the user
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    def __str__(self):
        return self.username
