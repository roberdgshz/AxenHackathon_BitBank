from django.views.generic import TemplateView
from django.shortcuts import render
from .models import Account

# Create your views here.
class ViewCompletation(TemplateView):
    template_name = 'account/completation.html'

class ViewAccount(TemplateView):
    template_name = 'account/account.html'

class ViewLogin(TemplateView):
    template_name = 'account/login.html'

class ViewSignup(TemplateView):
    template_name = 'account/signup.html'

def ViewRedirect(request):
    accounts = Account.objects.all()
    return render(request, 'account/username_accounts_verify.html', {'accounts': accounts})