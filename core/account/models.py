from users.models import User 
from django.db import models
import uuid
from shortuuid.django_fields import ShortUUIDField
from django_countries.fields import CountryField
from django.db.models.signals import post_save

ACCOUNT_STATUS = (
    ("active","Active"),
    ("in-active","In-Active"),
)

MARITAL_STATUS = (
    ("married","Married"),
    ("single","Single"),
    ("other","Other"),
)

GENDER = (
    ("male","Male"),
    ("female","Female"),
)

# NATIONALITY = (
#     ("active","Active"),
#     ("in-active","In-Active"),
# )

IDENTITY_TYPE = (
    ("national_id_card","National Id Card"),
    ("passport","Passport"),
)



#works as the upload_to argument
def user_dictionary_path(instance,filename):
    extenstion = filename.split(".")[-1]
    # splits the filename string by periods (.) and selects the last element 
    # of the resulting list, which represents the file extension.
    filename = "%s_%s" % (instance.id,extenstion)
    # creates a new filename by concatenating the instance.id 
    # with underscore (_) and the file extension.
    return "user_{0}/{1}".format(instance.user.id,filename)
    # returns a string representing the path where the file will be saved. 
    # The path is constructed using the instance.user.id
    
class Account(models.Model):
    id = models.UUIDField(primary_key=True,unique=True,default=uuid.uuid4,editable=False)
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    account_balance = models.DecimalField(max_digits=12,decimal_places=2,default=0.00)
    account_number = ShortUUIDField(length=10,max_length=15,unique=True,\
    prefix="151",alphabet="1234567890")
    account_id = ShortUUIDField(prefix="EG",length=10,unique=True,\
    max_length=14,alphabet="1234567890")
    pin_number = ShortUUIDField(length=4,alphabet="1234567890",unique=True,)
    ref_code = ShortUUIDField(length=7,max_length=10\
    ,unique=True,alphabet="abcdefg1234567890")
    nationality = CountryField(default="EG")    
    account_status = models.CharField(max_length=50,\
    choices=ACCOUNT_STATUS,default="in-active")
    date = models.DateTimeField(auto_now_add=True)
    kyc_submitted = models.BooleanField(default=False)
    kyc_confirmed = models.BooleanField(default=False)
    recommended_by = models.ForeignKey(User,on_delete=models.DO_NOTHING,\
    blank=True,null=True,related_name="recommended_by")
    gender = models.CharField(max_length=15,choices=GENDER)
    identity_type = models.CharField(max_length=100,choices=IDENTITY_TYPE)

    class Meta:
        ordering = ['-date']


def create_account(sender,instance,created,**kwargs):
    if created:
        Account.objects.create(user=instance)

def save_account(sender,instance,**kwargs):
    instance.account.save()

post_save.connect(create_account,sender=User)
post_save.connect(save_account,sender=User)