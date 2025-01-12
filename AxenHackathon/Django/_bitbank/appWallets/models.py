from django.db import models
from appAccounts.models import Account

# Create your models here.
class Coin(models.Model):
    coinid      = models.BigAutoField(primary_key=True)
    coinname    = models.CharField(max_length=100)
    coinkey     = models.CharField(max_length=5)
    coinimgpath = models.ImageField(upload_to='coins/', unique=True, null=True, blank=True)
    coinvalue   = models.DecimalField(max_digits=100,decimal_places=15)

    class Meta:
        db_table = "coin"

    def __str__(self):
        return self.coinname
    
class Wallet(models.Model):
    walletid         = models.BigAutoField(primary_key=True)
    walletaccountsid = models.ForeignKey(
        Account,
        on_delete=models.CASCADE,
    )
    walletcoinsid    = models.ForeignKey(
        Coin,
        on_delete=models.CASCADE,
    )
    walletcoinQuantity = models.BigIntegerField()
    walletbalance      = models.DecimalField(max_digits=100,decimal_places=20)

    class Meta:
        db_table = "wallet"

    def __str__(self):
        return f"Wallet {self.walletid} of {self.walletaccountsid}"
    
