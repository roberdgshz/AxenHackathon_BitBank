from django.db import models

# Create your models here.
class Account(models.Model):
    accountid       = models.BigAutoField(primary_key=True)
    accountusername = models.CharField(unique=True, max_length=255)
    accountpassword = models.CharField(max_length=255)
    accountemail    = models.CharField(unique=True, max_length=255)
    accountnip      = models.IntegerField()

    def __str__(self):
        return self.AccountUsername
    

class ProfileAccount(models.Model):
    ProfileID          = models.BigAutoField(primary_key=True)
    ProfileName        = models.CharField(max_length=255)
    ProfileLastname    = models.CharField(max_length=255)
    ProfileNumberphone = models.CharField(unique=True, max_length=15, blank=True, null=True)
    ProfileAccountid   = models.OneToOneField(
        Account,
        on_delete=models.CASCADE,
        unique=True    
    )

    def __str__(self):
        return f"{self.ProfileName} {self.ProfileLastname}"