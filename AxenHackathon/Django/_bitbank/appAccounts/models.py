from django.db import models

# Create your models here.
class Account(models.Model):
    accountid       = models.BigAutoField(primary_key=True)
    accountusername = models.CharField(unique=True, max_length=255)
    accountpassword = models.CharField(max_length=255)
    accountemail    = models.CharField(unique=True, max_length=255)
    accountnip      = models.IntegerField()

    class Meta:
        db_table = "account"

    def __str__(self):
        return self.accountusername
    

class ProfileAccount(models.Model):
    profileid          = models.BigAutoField(primary_key=True)
    profilename        = models.CharField(max_length=255)
    profilelastname    = models.CharField(max_length=255)
    profilenumberphone = models.CharField(unique=True, max_length=15, blank=True, null=True)
    profileaccountid   = models.OneToOneField(
        Account,
        on_delete=models.CASCADE,
        unique=True    
    )

    class Meta:
        db_table = "profile_account"

    def __str__(self):
        return f"{self.profilename} {self.profilelastname}"