from django.views.generic import TemplateView
from django.shortcuts import render

# Create your views here.
class ViewWalletCoinInfo(TemplateView):
    template_name = 'wallet/coin_info.html'

class ViewWalletCoinMarket(TemplateView):
    template_name = 'wallet/coin_market.html'

class ViewWalletCoin(TemplateView):
    template_name = 'wallet/wallet_coin.html'

class ViewWalletList(TemplateView):
    template_name = 'wallet/wallet_list.html'