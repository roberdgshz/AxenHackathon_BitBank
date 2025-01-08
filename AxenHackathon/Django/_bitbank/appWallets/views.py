from django.views.generic import TemplateView
from django.shortcuts import render, get_object_or_404
from .models import Coin

# Create your views here.
def ViewWalletCoinInfo(request, CoinID):
    moneda = get_object_or_404(Coin, CoinID=CoinID)
    return render(request, 'wallet/coin_info.html', {'coin': moneda})

def ViewWalletCoinMarket(request):
    monedas = Coin.objects.all()
    return render(request, 'wallet/coin_market.html', {'coins': monedas})

class ViewWalletCoin(TemplateView):
    template_name = 'wallet/wallet_coin.html'

class ViewWalletList(TemplateView):
    template_name = 'wallet/wallet_list.html'