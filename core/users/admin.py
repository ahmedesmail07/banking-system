from django.contrib import admin

from .models import User

class UserAdminView(admin.ModelAdmin):
    list_display = ["email","username"]

admin.site.register(User,UserAdminView)
