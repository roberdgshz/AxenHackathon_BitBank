from django.views.generic import TemplateView
from django.shortcuts import render
from .models import Account

# Create your views here.
class ViewCompletation(TemplateView):
    template_name = 'account/completation.html'

def ViewRedirect(request):
    accounts = Account.objects.all()
    return render(request, 'account/username_accounts_verify.html', {'accounts': accounts})

class ViewBase(TemplateView):
    template_name = 'base.html'