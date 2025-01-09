from django.views.generic import TemplateView
from django.shortcuts import render, get_object_or_404
from .models import Transaction
from appAccounts.models import Account

# Create your views here.
class ViewTransactionDeposit(TemplateView):
    template_name = 'transactions/transaction_deposit.html'

class ViewTransactionMenu(TemplateView):
    template_name = 'transactions/transaction_menu.html'

class ViewTransactionReceive(TemplateView):
    template_name = 'transactions/transaction_receive.html'

def ViewTransactionHistory(request, AccountUsername):
    user = get_object_or_404(Account, AccountUsername=AccountUsername)
    transactions = Transaction.objects.all()
    return render(request, 'transactions/transaction_history.html', {'user':user, 'transactions':transactions})

def ViewTransactionInfo(request, TransactionID):
    transaction = get_object_or_404(Transaction, TransactionID=TransactionID)
    return render(request, 'transactions/transaction_info.html', {'transaction':transaction})
