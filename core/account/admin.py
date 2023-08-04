from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Account , KYC

class AccountAdmin(ImportExportModelAdmin):
    list_editable = ['account_balance','account_status','identity_type']
    list_display= ['user','account_id','account_balance','account_status','identity_type']
    list_filter=['user','account_balance']

admin.site.register(Account,AccountAdmin)

class KYCAdmin(ImportExportModelAdmin):
    # model = Account
    search_fields = ['full_name']
    list_display= ['user','full_name']

admin.site.register(KYC,KYCAdmin)