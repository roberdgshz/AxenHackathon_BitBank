from django.db import models

from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager)

# Create your models here.

# Custom user
class UserManager(BaseUserManager):
    def create_user(self, email, AccountUsername, AccountNip, password=None, is_staff=False, is_admin=False, active=True):
        if not email:
            raise ValueError("Users must have an email address")
        if not password:
            raise ValueError("Users must have a password")
        if not AccountUsername:
            raise ValueError("Users must have an username")
        if not AccountNip:
            raise ValueError("Users must have a nip")
        user_obj = self.model(email = self.normalize_email(email), AccountUsername = AccountUsername, AccountNip = AccountNip)
        user_obj.set_password(password)
        user_obj.staff = is_staff
        user_obj.admin = is_admin
        user_obj.is_active = active
        user_obj.save(using = self._db)
        return user_obj
    
    def create_staffuser(self, email, AccountUsername, AccountNip, password=None):
        user = self.create_user(
            email, AccountUsername, AccountNip, password=password,
            is_staff=True
        )
        return user
    
    def create_superuser(self, email, AccountUsername, AccountNip, password=None):
        user = self.create_user(
            email, AccountUsername, AccountNip, password=password,
            is_staff=True,
            is_admin=True
        )
        return user

class Account(AbstractBaseUser):
    AccountID = models.BigAutoField(primary_key=True)
    AccountUsername = models.CharField(unique=True, max_length=255, null=True)
    email = models.EmailField(unique=True, max_length=255, db_column='email')
    AccountNip = models.IntegerField(null=True)
    is_active = models.BooleanField(default=True)
    staff = models.BooleanField(default=False)
    admin = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['AccountUsername', 'AccountNip']

    objects = UserManager()

    def __str__(self):
        return self.AccountUsername or ""
    
    def get_full_name(self):
        return self.AccountUsername
    
    def get_short_name(self):
        return self.AccountUsername
    
    def has_perm(self, perm, obj=None):
        return True
    
    def has_module_perms(self, app_label):
        return True
    
    @property
    def is_staff(self):
        return self.staff
    @property
    def is_admin(self):
        return self.admin
    
    @property
    def active(self):
        return self.is_active
    
class ProfileAccount(models.Model):
    ProfileID = models.BigAutoField(primary_key=True)
    ProfileName = models.CharField(max_length=255)
    ProfileLastname = models.CharField(max_length=255)
    ProfileNumberphone = models.CharField(unique=True, max_length=15, blank=True, null=True)
    ProfileAccountid = models.OneToOneField(
        Account,
        on_delete=models.CASCADE,
        unique=True    
    )

    def __str__(self):
        return f"{self.ProfileName} {self.ProfileLastname}"