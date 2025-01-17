# services.py
import requests
from .models import Coin
import time
from threading import Thread
from django.db import transaction, connection
import os
from decimal import Decimal

cmc_api_key = os.environ.get('CMC_API_KEY')

class CryptoUpdateService:
    def __init__(self):
        self.headers = {
            'X-CMC_PRO_API_KEY': #Api de las criptomonedas
            'Accepts': 'application/json'
        }
        self.params = {
            'start': '1',
            'limit': '5',
            'convert': 'USD'
        }
        self.url = #Api de las criptomonedas
        
        self.coin_mapping = {
            'BTC': {
                'name': 'Bitcoin',
                'image': 'coins/bitcoin.png'
            },
            'ETH': {
                'name': 'Ethereum',
                'image': 'coins/ethereum.png'
            },
            'XRP': {
                'name': 'XRP',
                'image': 'coins/xrp.png'
            },
            'USDT': {
                'name': 'Tether USDT',
                'image': 'coins/tetherusdt.png'
            },
            'BNB': {
                'name': 'BNB',
                'image': 'coins/bnb.png'
            }
        }

    def update_prices(self):
        try:
            response = requests.get(self.url, params=self.params, headers=self.headers)
            data = response.json()
            
            if response.status_code == 200:
                with transaction.atomic():
                    for coin_data in data['data']:
                        symbol = coin_data['symbol']
                        price = round(coin_data['quote']['USD']['price'], 2)
                            
                           
                        Coin.objects.update_or_create(
                            coinkey=symbol,
                            defaults={
                                'coinname': self.coin_mapping[symbol]['name'],
                                'coinimgpath': self.coin_mapping[symbol]['image'],
                                'coinvalue': price
                            }
                        )
                
                return True
        except Exception as e:
            print(f"Error updating prices: {e}")
            return False

    def start_update_thread(self):
        def update_loop():
            while True:
                self.update_prices()
                self.update_coin_values()
                self.update_allwallets()
                time.sleep(60)

        thread = Thread(target=update_loop, daemon=True)
        thread.start()
        
    def update_MXNcoin_value(target_currency):
        url = #Api de las monedas nacionales
        headers = {"accept": "application/json"}
        response = requests.get(url, headers=headers)

        try:
            response = requests.get(url, headers=headers)
            response.raise_for_status()  # Manejar errores HTTP
        except requests.RequestException as e:
            print(f"Error al consultar la API: {e}")
            return  

        data = response.json()
        result = data.get("result", {})
        updated_value = result.get(target_currency)

        if updated_value is not None:
            currency_map = {
                "MXN": "Mexican Peso",
                "USD": "US Dollar",

            }
            coinname = currency_map.get(target_currency, "Unknown")

            Coin.objects.update_or_create(
                coinkey=target_currency,
                defaults={
                    "coinname": coinname,
                    "coinvalue": updated_value,
                }
            )
        else:
            pass
        
    def update_coin_values(self):
        url = #Api de las monedas nacionales
        headers = {"accept": "application/json"}
        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            data = response.json()
            results = data.get("results", {})

        currency_map = {
            "MXN": "Mexican Peso",
            "EUR": "Euro",
            "CAD": "Canadian Dollar",
            "CNY": "Chinese Yuan",
            "JPY": "Japanese Yen",
            "KRW": "Surkorean Won",
            "RUB": "Russian Rublo",
        }

        for coinkey, coinvalue in results.items():
            coinname = currency_map.get(coinkey, "Unknown")
            Coin.objects.update_or_create(
                coinkey=coinkey,
                defaults={
                    "coinname": coinname,
                    "coinvalue": coinvalue,
                }
            )
        else:
            return None  
    
    def update_allwallets(self):
        with connection.cursor() as cursor:
            cursor.execute("SELECT w.walletid, w.walletaccountsid_id, w.walletcoinsid_id, w.walletbalance, w.walletcoinquantity, c.coinvalue FROM wallet w JOIN coin c ON w.walletcoinsid_id = c.coinid;")
            resultados = cursor.fetchall()

        for fila in resultados:
            walletid = fila[0]
            userid = fila[1]
            coinid = fila[2]
            quantity = Decimal(fila[4])  
            coinvalue = Decimal(fila[5]) 

            newbalance = coinvalue * quantity

            with connection.cursor() as cursor:
                cursor.execute("UPDATE wallet SET walletbalance = %s WHERE walletid = %s AND walletaccountsid_id = %s", [newbalance, walletid, userid])
