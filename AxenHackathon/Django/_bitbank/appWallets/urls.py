from django.urls import path
from .views import *

urlpatterns = [
    path('coin_info/<int:id>', ViewWalletCoinInfo, name="coin_info"),
    path('coin_market/', ViewWalletCoinMarket, name="coin_market"),
    path('wallet_coin/<int:walletid>', ViewWalletCoin, name="wallet_coin"),
    path('wallet_list/<str:user>', ViewWalletList, name="wallet_list"),
]