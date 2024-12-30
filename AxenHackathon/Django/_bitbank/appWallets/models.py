from django.db import models

# Create your models here.
class Coin(models.Model):
    CoinID      = models.BigAutoField(primary_key=True)
    CoinName    = models.CharField(max_length=100)
    CoinKey     = models.CharField(max_length=5)
    CoinImgPath = models.CharField(max_length=255, unique=True, null=True, blank=True)
    CoinValue   = models.BigIntegerField()

    def __str__(self):
        return self.CoinName
    
class Wallet(models.Model):
    WalletID         = models.BigAutoField(primary_key=True)
    WalletAccountsID = models.BigIntegerField() #It remains to make it foreign key
    WalletCoinsID    = models.OneToOneField(
        Coin,
        on_delete=models.CASCADE,
        unique=True
    )
    WalletCoinQuantity = models.BigIntegerField()
    WalletBalance       = models.BigIntegerField()

    def __str__(self):
        return f"Wallet {self.WalletID} of {self.WalletAccountsID}"
    