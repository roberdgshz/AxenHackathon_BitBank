from django.db import models
from appAccounts.models import Account
from appWallets.models import Coin

# Create your models here.
class Transaction(models.Model):
    TransactionID          = models.BigAutoField(primary_key=True)
    TransactionAmount      = models.BigIntegerField()
    TransactionCoin        = models.ForeignKey(
        Coin,
        on_delete=models.CASCADE
    )
    TransactionDate        = models.DateTimeField()
    TransactionReceiver    = models.ForeignKey(
        Account,
        on_delete=models.CASCADE,
        related_name="receiver"
    )
    TransactionTransmitter = models.ForeignKey(
        Account,
        on_delete=models.CASCADE,
        related_name="transmitter"
    )

    def __str__(self):
        return f"{self.TransactionTransmitter} to {self.TransactionReceiver}, Amount: {self.TransactionAmount}. {self.TransactionDate}"