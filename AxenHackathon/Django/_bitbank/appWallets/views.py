from django.shortcuts import render, get_object_or_404
from .models import Coin, Wallet
from appAccounts.models import Account

# Create your views here.
def ViewWalletCoinInfo(request, CoinID):
    moneda = get_object_or_404(Coin, CoinID=CoinID)
    return render(request, 'wallet/coin_info.html', {'coin': moneda})

def ViewWalletCoinMarket(request):
    monedas = Coin.objects.all()
    return render(request, 'wallet/coin_market.html', {'coins': monedas})

def ViewWalletList(request, AccountUsername):
    user = get_object_or_404(Account, AccountUsername=AccountUsername)
    wallets = Wallet.objects.all()
    return render(request, 'wallet/wallet_list.html', {'user':user, 'wallets':wallets})

def ViewWalletCoin(request, WalletID):
    wallet = get_object_or_404(Wallet, WalletID=WalletID)
    return render(request, 'wallet/wallet_coin.html', {'wallet':wallet})
