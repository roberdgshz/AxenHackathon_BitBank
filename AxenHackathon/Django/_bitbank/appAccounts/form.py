# forms.py
from django import forms
from .models import Account

class CustomUserCreationForm(forms.ModelForm):
    email = forms.EmailField(required=True)
    accountusername = forms.CharField(max_length=255, required=True, label="username")
    accountnip = forms.IntegerField(required=True, label="nip")
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = Account
        fields = ['email', 'accountusername', 'accountnip']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user