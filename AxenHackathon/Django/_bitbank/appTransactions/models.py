from django.db import models
from appAccounts.models import Account
from appWallets.models import Coin

# Create your models here.
class Transaction(models.Model):
    transactionid          = models.BigAutoField(primary_key=True)
    transactionamount      = models.DecimalField(max_digits=100,decimal_places=50)
    transactioncoin        = models.ForeignKey(
        Coin,
        on_delete=models.CASCADE
    )
    transactiondate        = models.DateTimeField()
    transactionreceiver    = models.ForeignKey(
        Account,
        on_delete=models.CASCADE,
        related_name="receiver"
    )
    transactiontransmitter = models.ForeignKey(
        Account,
        on_delete=models.CASCADE,
        related_name="transmitter"
    )

    def __str__(self):
        return f"{self.transactiontransmitter} to {self.transactionreceiver}, Amount: {self.transactionamount}. {self.transactiondate}"