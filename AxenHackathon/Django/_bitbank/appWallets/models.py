from django.db import models
from appAccounts.models import Account

# Create your models here.
class Coin(models.Model):
    CoinID      = models.BigAutoField(primary_key=True)
    CoinName    = models.CharField(max_length=100)
    CoinKey     = models.CharField(max_length=5)
    CoinImgPath = models.ImageField(upload_to='coins/', unique=True, null=True, blank=True)
    CoinValue   = models.BigIntegerField()

    def __str__(self):
        return self.CoinName
    
class Wallet(models.Model):
    WalletID         = models.BigAutoField(primary_key=True)
    WalletAccountsID = models.ForeignKey(
        Account,
        on_delete=models.CASCADE,
    )
    WalletCoinsID    = models.ForeignKey(
        Coin,
        on_delete=models.CASCADE,
    )
    WalletCoinQuantity = models.BigIntegerField()
    WalletBalance      = models.BigIntegerField()

    def __str__(self):
        return f"Wallet {self.WalletID} of {self.WalletAccountsID}"
    
