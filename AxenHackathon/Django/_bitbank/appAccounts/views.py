from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.contrib.auth.models import User

from django.db import connection
from .models import Account

# Create your views here.
class ViewCompletation(TemplateView):
    template_name = 'account/completation.html'

def ViewAccount(request, user):
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM account WHERE accountusername = %s",[user])
        resultados = cursor.fetchall()
    
    cuenta = [
        {"id":fila[0],"username":fila[1],"password":fila[2],"email":fila[3],"nip":fila[4]}
        for fila in resultados
    ]

    return render(request, 'account/account.html', {'user':cuenta})

def ViewLoginUser(request):
    if request.method == 'POST':
        username_or_email = request.POST.get('username')
        password = request.POST.get('password')

        if not username_or_email or not password:
            messages.error(request, "Both username/email and password are required.")
            return redirect('login')

        user = User.objects.filter(email=username_or_email).first()
        if user:
            username = user.username  
        else:
            username = username_or_email 

        # Autentica al usuario
        authenticated_user = authenticate(request, username=username, password=password)
        if authenticated_user is not None:
            login(request, authenticated_user)
            messages.success(request, "Login successful!")
            return redirect('home')
        else:
            messages.error(request, "Invalid email/username or password.")
            return redirect('login')

    return render(request, 'account/login.html')

def ViewRegisterUser(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        username = request.POST.get('AccountUsername')
        nip = request.POST.get('AccountNip')  
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        # Validaciones básicas
        if password1 != password2:
            messages.error(request, "Passwords do not match.")
            return redirect('register')

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already taken.")
            return redirect('register')

        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already in use.")
            return redirect('register')

        # Crear usuario
        with connection.cursor() as cursor:
            cursor.execute("SELECT insert_user_account('"+username+"','"+password1+"','"+email+"',"+nip+");")
 
        #user = authenticate(request, username=username, password=password1)
        #login(request,user)
        messages.success(request, "Registration successful!")
        return redirect('login')

    return render(request, 'account/signup.html')

def ViewRedirect(request):
    accounts = Account.objects.all()
    return render(request, 'account/username_accounts_verify.html', {'accounts': accounts})