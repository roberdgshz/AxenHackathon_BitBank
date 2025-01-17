from django.db import models

from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager)

# Create your models here.

# Custom user
class UserManager(BaseUserManager):
    def create_user(self, email, accountusername, accountnip, password=None, is_staff=False, is_admin=False, active=True):
        if not email:
            raise ValueError("Users must have an email address")
        if not password:
            raise ValueError("Users must have a password")
        if not accountusername:
            raise ValueError("Users must have an username")
        if not accountnip:
            raise ValueError("Users must have a nip")
        user_obj = self.model(email = self.normalize_email(email), accountusername = accountusername, accountnip = accountnip)
        user_obj.set_password(password)
        user_obj.staff = is_staff
        user_obj.admin = is_admin
        user_obj.is_active = active
        user_obj.save(using = self._db)
        return user_obj
    
    def create_staffuser(self, email, accountusername, accountnip, password=None):
        user = self.create_user(
            email, accountusername, accountnip, password=password,
            is_staff=True
        )
        return user
    
    def create_superuser(self, email, accountusername, accountnip, password=None):
        user = self.create_user(
            email, accountusername, accountnip, password=password,
            is_staff=True,
            is_admin=True
        )
        return user

class Account(AbstractBaseUser):
    accountid = models.BigAutoField(primary_key=True)
    accountusername = models.CharField(unique=True, max_length=255)
    email = models.EmailField(unique=True, max_length=255, db_column='email')
    accountnip = models.IntegerField(null=True)
    is_active = models.BooleanField(default=True)
    staff = models.BooleanField(default=False)
    admin = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['accountusername', 'accountnip']

    objects = UserManager()

    class Meta:
        db_table = "account"

    def __str__(self):
        return self.accountusername
    
    def get_full_name(self):
        return self.accountusername
    
    def get_short_name(self):
        return self.accountusername
    
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