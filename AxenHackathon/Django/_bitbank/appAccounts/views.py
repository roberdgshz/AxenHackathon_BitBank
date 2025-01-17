from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.contrib.auth.models import User

from django.db import connection
from .models import Account

from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .form import CustomUserCreationForm
from django.contrib.auth import login
from django.contrib.auth import authenticate, logout

from django.db import connection

# Create your views here.
class ViewCompletation(TemplateView):
    template_name = 'account/completation.html'

def ViewAccount(request):
    if request.user.is_authenticated:
         current_user = Account.objects.get(accountid=request.user.accountid)
         form = CustomUserCreationForm(request.POST or None, instance=current_user)
         if form.is_valid():
            form.save()
            login(request, current_user)
            messages.success(request, ("Your information has been updated"))
            return redirect('home')

         return render(request, 'account/account.html', {'form':form})
    else:
        messages.success(request, ("You must be logged in"))
        return redirect('home')

def ViewLoginUser(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, username=email, password=password)
        if user is not None:
            with connection.cursor() as cursor:
                cursor.execute("SELECT accountid FROM account WHERE email = %s",[email])
                userid = cursor.fetchone()
            if userid:
                with connection.cursor() as cursor:
                    cursor.execute("SELECT insert_log_login(%s,%s)",[email,userid[0]])
            else: pass
            login(request, user)
            return redirect('home')
    return render(request, 'account/login.html')

def ViewRegisterUser(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = CustomUserCreationForm()
    return render(request, 'account/signup.html', {'form':form})

def ViewRedirect(request):
    accounts = Account.objects.all()
    return render(request, 'account/username_accounts_verify.html', {'accounts': accounts})