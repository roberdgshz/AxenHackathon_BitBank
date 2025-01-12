from django.views.generic import TemplateView
from django.shortcuts import render

from django.db import connection

# Create your views here.
class ViewTransactionDeposit(TemplateView):
    template_name = 'transactions/transaction_deposit.html'

class ViewTransactionMenu(TemplateView):
    template_name = 'transactions/transaction_menu.html'

class ViewTransactionReceive(TemplateView):
    template_name = 'transactions/transaction_receive.html'

def ViewTransactionHistory(request, user):
    with connection.cursor() as cursor:
        cursor.execute("SELECT accountid FROM account WHERE accountusername = %s;",[user])
        user_id = cursor.fetchone()

    if user_id:
        user_id = user_id[0]
    else:
        return []

    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM transaction WHERE transactiontransmitter_id = %s OR transactionreceiver_id = %s;",
                       [user_id, user_id])
        resultados = cursor.fetchall()
    
    transacciones = [
        {"id": fila[0], "date":fila[1], "receiver":fila[2], "transmitter":fila[3], "coinid":fila[4], "amount":fila[5], "status":fila[6]}
        for fila in resultados
    ]

    return render(request, 'transactions/transaction_history.html', {'userid':user_id, 'transactions':transacciones})

def ViewTransactionInfo(request, id):
    with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM transaction WHERE transactionid = %s;",[id])
            resultado = cursor.fetchone()
    
    if resultado :
        transaccion = {"id": resultado[0], "date":resultado[1], "receiver":resultado[2], "transmitter":resultado[3], "coinid":resultado[4], "amount":resultado[5], "status":resultado[6]}

    return render(request, 'transactions/transaction_info.html', {'transaction':transaccion})
