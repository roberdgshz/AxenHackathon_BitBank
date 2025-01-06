# forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Account

class CustomUserCreationForm(UserCreationForm):
    AccountUsername = forms.CharField(max_length=255, required=True, label="Username")
    AccountNip = forms.IntegerField(required=True, label="NIP")

    class Meta:
        model = Account
        fields = ['email', 'AccountUsername', 'AccountNip', 'password1', 'password2']
