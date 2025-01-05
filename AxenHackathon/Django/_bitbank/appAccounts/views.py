from django.views.generic import TemplateView
from django.shortcuts import render, get_object_or_404

from .models import Account
from django.http import JsonResponse

# Create your views here.
class ViewCompletation(TemplateView):
    template_name = 'account/completation.html'

def ViewValidateUsername(request):
    if request.method == 'POST':
        username = request.POST.get('username', '').strip()
        if not username:
            return render(request, 'template.html', {'error': 'Username is required.'})

        if Account.objects.filter(AccountUsername=username).exists():
            return render(request, 'account/username_accounts_verify.html', {'error': 'Username already exists. Please choose another one.'})

        return render(request, 'account/username_accounts_verify.html', {'error': 'Username is available!'})
    
    return render(request, 'account/username_accounts_verify.html')

class ViewBase(TemplateView):
    template_name = 'base.html'