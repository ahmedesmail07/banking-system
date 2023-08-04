from django.contrib import admin

from .models import Account

class AccountAdmin(admin.ModelAdmin):
    list_editable = ['account_balance','account_status','identity_type']
    list_display= ['user','account_id','account_balance','account_status','identity_type']
    list_filter=['user','account_balance']

admin.site.register(Account,AccountAdmin)
