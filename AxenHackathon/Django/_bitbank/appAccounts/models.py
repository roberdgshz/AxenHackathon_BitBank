from django.db import models

# Create your models here.
class Account(models.Model):
    AccountID       = models.BigAutoField(primary_key=True)
    AccountUsername = models.CharField(unique=True, max_length=255)
    AccountPassword = models.CharField(max_length=255)
    AccountEmail    = models.CharField(unique=True, max_length=255)
    AccountNip      = models.IntegerField()

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