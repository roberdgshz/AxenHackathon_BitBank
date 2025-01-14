from django.shortcuts import render

from django.db import connection

# Create your views here.
def ViewWalletCoinInfo(request, id):
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM coin WHERE coinid = %s;",[id])
        resultado = cursor.fetchone()

    if resultado :
        moneda = {"id":resultado[0], "name":resultado[1], "key":resultado[2], "img":resultado[3], "value":resultado[4]}

    return render(request, 'wallet/coin_info.html', {'coin': moneda})

def ViewWalletCoinMarket(request):
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM coin")
        resultados = cursor.fetchall()
    
    monedas = [
        {"id":fila[0], "name":fila[1], "key":fila[2], "img":fila[3], "value":fila[4]}
        for fila in resultados
    ]

    return render(request, 'wallet/coin_market.html', {'coins': monedas})

def ViewWalletList(request, user):
    with connection.cursor() as cursor:
        cursor.execute("SELECT accountid FROM account WHERE accountusername = %s;",[user])
        user_id = cursor.fetchone()

    if user_id:
        user_id = user_id[0]
    else:
        return []

    with connection.cursor() as cursor:
        cursor.execute("""SELECT *, c.coinname FROM wallet 
		    JOIN coin c ON wallet.walletcoinsid_id = c.coinid 
			    WHERE walletaccountsid_id = %s""",[user_id])
        resultados = cursor.fetchall()

    wallets = [
        {"id":fila[0], "balance":fila[1], "quantity":fila[4], "coinname":fila[6], "coinkey":fila[7]}
        for fila in resultados
    ]

    return render(request, 'wallet/wallet_list.html', {'wallets':wallets})

def ViewWalletCoin(request, walletid):
    with connection.cursor() as cursor:
        cursor.execute("""SELECT *, c.coinname FROM wallet 
		    JOIN coin c ON wallet.walletcoinsid_id = c.coinid 
			    WHERE walletid = %s""",[walletid])
        resultado = cursor.fetchone()

    if resultado :
        wallet = {"id":resultado[0], "balance":resultado[1], "accountid":resultado[2], "coinid":resultado[3], "quantity":resultado[4], "coinname":resultado[6], "coinkey":resultado[7]}

    return render(request, 'wallet/wallet_coin.html', {'wallet':wallet})
