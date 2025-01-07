from django.views.generic import TemplateView
from django.shortcuts import render

# Create your views here.
class ViewTransactionDeposit(TemplateView):
    template_name = 'transactions/transaction_deposit.html'

class ViewTransactionHistory(TemplateView):
    template_name = 'transactions/transaction_history.html'

class ViewTransactionInfo(TemplateView):
    template_name = 'transactions/transaction_info.html'

class ViewTransactionMenu(TemplateView):
    template_name = 'transactions/transaction_menu.html'

class ViewTransactionReceive(TemplateView):
    template_name = 'transactions/transaction_receive.html'