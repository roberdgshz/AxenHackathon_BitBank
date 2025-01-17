from django.shortcuts import render
from django.db import connection
from .services import CryptoUpdateService

from django.shortcuts import render
from django.db import connection
import plotly.graph_objects as go
import json
import requests
from datetime import datetime, timedelta

#crypto_service = CryptoUpdateService()
#crypto_service.start_update_thread()

# Create your views here.
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
        cursor.execute("SELECT *, c.coinname FROM wallet JOIN coin c ON wallet.walletcoinsid_id = c.coinid WHERE walletid = %s;",[walletid])
        resultado = cursor.fetchone()

    if resultado :
        wallet = {"id":resultado[0], "balance":resultado[1], "coinid":resultado[3], "quantity":resultado[4], "coinname":resultado[6], "coinkey":resultado[7]}

    return render(request, 'wallet/wallet_coin.html', {'wallet':wallet})


def get_historical_prices(coin_key):
    headers = {
        'X-CMC_PRO_API_KEY': #Api de las criptomonedas
        'Accepts': 'application/json'
    }
    
    url = #Api de las criptomonedas
    params = {
        'symbol': coin_key,
        'convert': 'USD'
    }
    
    response = requests.get(url, params=params, headers=headers)
    data = response.json()
    
    if response.status_code == 200:
        quote = data['data'][coin_key]['quote']['USD']
        current_price = quote['price']
        
        prices = []
        dates = []
        
        # List of periods in days and their corresponding fields in the API
        periods = [
            (90, 'percent_change_90d'),
            (60, 'percent_change_60d'),
            (30, 'percent_change_30d'),
            (7, 'percent_change_7d'),
            (1, 'percent_change_24h'),
            (0.0417, 'percent_change_1h')
        ]
        
        for days, change_field in periods:
            if change_field in quote:
                change = quote[change_field]
                if change is not None:
                    # Calculate historical price
                    historical_price = current_price / (1 + change/100)
                    prices.append(historical_price)
                    date = datetime.now() - timedelta(days=days)
                    dates.append(date)
        
        # Add current price
        prices.append(current_price)
        dates.append(datetime.now())
        
        return dates, prices
    return None, None

def ViewWalletCoinInfo(request, id):
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM coin WHERE coinid = %s;", [id])
        resultado = cursor.fetchone()

    if resultado:
        moneda = {"id": resultado[0], "name": resultado[1], "key": resultado[2], "img": resultado[3], "value": resultado[4]}
        
        dates, prices = get_historical_prices(moneda['key'])
        
        if dates and prices:
            # create the graph
            fig = go.Figure()
            fig.add_trace(go.Scatter(
                x=dates,
                y=prices,
                mode='lines+markers',
                name=moneda['key']
            ))
            
            fig.update_layout(
                title=f'{moneda["name"]} Price History',
                xaxis_title='Date',
                yaxis_title='Price (USD)',
                template='plotly_white',
                hovermode='x unified'
            )
            
            # Convert the graph to HTML
            plot_div = fig.to_html(full_html=False)
            
            return render(request, 'wallet/coin_info.html', {
                'coin': moneda,
                'plot_div': plot_div
            })
    return render(request, 'wallet/coin_info.html', {'coin': moneda})
