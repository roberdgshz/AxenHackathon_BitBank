from django.db import models
from appAccounts.models import Account
from appWallets.models import Coin

# Create your models here.
class TransactionStatus(models.Model):
    transactionstatusid = models.IntegerField(primary_key=True)
    transactionstatus = models.CharField()

    class Meta:
        db_table = "transaction_status"

    def __str__(self):
        return self.transactionstatus

class Transaction(models.Model):
    transactionid          = models.BigAutoField(primary_key=True)
    transactionamount      = models.DecimalField(max_digits=100,decimal_places=2)
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
    transactionstatus = models.ForeignKey(
        TransactionStatus,
        on_delete=models.CASCADE,
    )

    class Meta:
        db_table = "transaction"

    def __str__(self):
        return f"{self.transactiontransmitter} to {self.transactionreceiver}, Amount: {self.transactionamount}, {self.transactioncoin}. {self.transactiondate}"