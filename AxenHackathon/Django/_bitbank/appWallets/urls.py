from django.urls import path
from .views import *

urlpatterns = [
    path('coin_info/<int:CoinID>', ViewWalletCoinInfo, name="coin_info"),
    path('coin_market/', ViewWalletCoinMarket, name="coin_market"),
    path('wallet_coin/', ViewWalletCoin.as_view(), name="wallet_coin"),
    path('wallet_list/', ViewWalletList.as_view(), name="wallet_list"),
]