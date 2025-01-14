from django.views.generic import TemplateView
from django.shortcuts import render

from django.db import connection
from django.contrib import messages
from decimal import Decimal

# Create your views here.
def ViewTransactionDeposit(request, user):
    with connection.cursor() as cursor:
        cursor.execute("SELECT coinid, coinname, coinkey FROM coin")
        resultados = cursor.fetchall()
    
    monedas = [
        {"id":fila[0], "name":fila[1], "key":fila[2]}
        for fila in resultados
    ]

    return render(request, 'transactions/transaction_deposit.html', {'coins':monedas, "user":user})

class ViewTransactionMenu(TemplateView):
    template_name = 'transactions/transaction_menu.html'

def ViewTransactionReceive(request, user):
    with connection.cursor() as cursor:
        cursor.execute("SELECT coinid, coinname, coinkey FROM coin")
        resultados = cursor.fetchall()
    
    monedas = [
        {"id":fila[0], "name":fila[1], "key":fila[2]}
        for fila in resultados
    ]

    return render(request, 'transactions/transaction_receive.html', {"coins":monedas, "user":user})

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

def ViewTransactionDepositGenerator(request):
    if request.method == 'POST':
        amount = request.POST.get('amount')
        currency = request.POST.get('currency')
        receiver = request.POST.get('receiver')
        user = request.POST.get('username')

        with connection.cursor() as cursor: # This is to search the transmitter's id
            cursor.execute("SELECT accountid FROM account WHERE accountusername = %s",[user])
            id = cursor.fetchone()

        with connection.cursor() as cursor: # This is to search the available's quantity of the transmitter
            cursor.execute("SELECT walletcoinquantity FROM wallet WHERE walletaccountsid_id = %s AND walletcoinsid_id = %s",[id[0], currency])
            availableamount = cursor.fetchone()
        
        if availableamount :
            if availableamount[0] >= Decimal(amount) :
                with connection.cursor() as cursor: # This is to search the receiver's id
                    cursor.execute("SELECT accountid FROM account WHERE accountusername = %s",[receiver])
                    idreceiver = cursor.fetchone()

                with connection.cursor() as cursor: # This is to search if the receiver already has a wallet with the specific coin
                    cursor.execute("SELECT * FROM wallet WHERE walletcoinsid_id = %s AND walletaccountsid_id = %s",[currency, idreceiver[0]])
                    walletreceiver = cursor.fetchone()

                with connection.cursor() as cursor: # This is to get the value of the coin
                    cursor.execute("SELECT coinvalue FROM coin WHERE coinid = %s",[currency])
                    coinvalue = cursor.fetchone()

                if walletreceiver:
                    with connection.cursor() as cursor: # This is to search the available's quantity of the receiver
                        cursor.execute("SELECT walletcoinquantity FROM wallet WHERE walletaccountsid_id = %s AND walletcoinsid_id = %s",[idreceiver[0], currency])
                        totalamount = cursor.fetchone()

                    transmitternewavailableamount = availableamount[0] - Decimal(amount)
                    receivernewtotalamount = totalamount[0] + Decimal(amount)

                    transmitternewbalance = transmitternewavailableamount * coinvalue[0]
                    receivernewbalance = receivernewtotalamount * coinvalue[0]

                    with connection.cursor() as cursor: # This is to alter the table with the new quantity's and values
                        cursor.execute("SELECT alter_wallet(%s,%s,%s,%s,%s,%s,%s)",[currency,id[0],idreceiver[0],transmitternewavailableamount,receivernewtotalamount,transmitternewbalance,receivernewbalance])

                else :
                    receiverbalance = coinvalue[0] * Decimal(amount)
                    
                    transmitternewavailableamount = availableamount[0] - Decimal(amount)
                    transmitternewbalance = transmitternewavailableamount * coinvalue[0]

                    with connection.cursor() as cursor:
                        cursor.execute("SELECT insert_wallet(%s,%s,%s,%s)",[receiverbalance,idreceiver[0],currency,amount])
                    
                    with connection.cursor() as cursor:
                        cursor.execute("UPDATE wallet SET walletcoinquantity = %s, walletbalance = %s WHERE walletaccountsid_id = %s AND walletcoinsid_id = %s",[transmitternewavailableamount,transmitternewbalance,id[0],currency])
            else:
                messages.error(request, "Not enough quantity available!")
        else :
            messages.error(request, "Not enough quantity available!")
        
        with connection.cursor() as cursor:
            cursor.execute("SELECT coinkey FROM coin WHERE coinid = %s",[currency])
            coin = cursor.fetchone()

        description = user+" made a transaction of "+str(amount)+" "+str(coin[0])+" to "+receiver

        with connection.cursor() as cursor:
            cursor.execute("SELECT insert_notification_transaction(%s,%s,%s)",[description,id,idreceiver[0]])
    return render(request, 'transactions/transaction_deposit_generator.html')

def ViewTransactionReceiveGenerator(request):
    if request.method == 'POST':
        amount = request.POST.get('amount')
        currency = request.POST.get('currency')
        user = request.POST.get('username')

        with connection.cursor() as cursor:
            cursor.execute("SELECT accountid FROM account WHERE accountusername = %s",[user])
            id = cursor.fetchone()

        with connection.cursor() as cursor:
            cursor.execute("SELECT coinvalue FROM coin WHERE coinid = %s",[currency])
            coinid = cursor.fetchone()

        balance = coinid[0] * Decimal(amount)

        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM wallet WHERE walletcoinsid_id = %s AND walletaccountsid_id = %s",[currency,id])
            wallet = cursor.fetchone()

        if wallet :

            newquantity = wallet[4] + Decimal(amount)
            newbalance = newquantity * coinid[0]
            
            with connection.cursor() as cursor:
                cursor.execute("UPDATE wallet SET walletcoinquantity = %s, walletbalance = %s WHERE walletaccountsid_id = %s AND walletcoinsid_id = %s", [newquantity,newbalance,id,currency])
        else:
            with connection.cursor() as cursor:
                cursor.execute("SELECT insert_wallet(%s,%s,%s,%s)",[balance,id,currency,amount])
                    
        with connection.cursor() as cursor:
            cursor.execute("SELECT coinkey FROM coin WHERE coinid = %s",[currency])
            coin = cursor.fetchone()

        description = "Bitbank made a transaction of "+str(amount)+" "+str(coin[0])+" to "+user

        with connection.cursor() as cursor:
            cursor.execute("SELECT insert_log_transactionreceiver(%s,%s)",[description,id])

        with connection.cursor() as cursor:
            cursor.execute("SELECT insert_transaction_folio(%s,%s,%s)",[id,amount,currency])

    return render(request, 'transactions/transaction_receive_generator.html')