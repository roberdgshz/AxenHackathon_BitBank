# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

class Accounts(models.Model):
    accountid = models.BigAutoField(primary_key=True)
    accountusername = models.CharField(unique=True, max_length=255)
    accountpassword = models.CharField(max_length=255)
    accountemail = models.CharField(unique=True, max_length=255)
    accountnip = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'Accounts'


class Auditlogs(models.Model):
    auditlogid = models.BigAutoField(primary_key=True)
    auditlogaccount = models.OneToOneField(Accounts, models.DO_NOTHING, db_column='auditlogaccount')
    auditlogdescription = models.TextField()
    auditlogtime = models.TimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'AuditLogs'

        
class Coins(models.Model):
    coinidbig = models.AutoField(primary_key=True)
    coinname = models.CharField(max_length=100)
    coinkey = models.CharField(max_length=5)
    coinimgpath = models.CharField(unique=True, max_length=255, blank=True, null=True)
    coinvalue = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'Coins'


class Profileaccounts(models.Model):
    profileid = models.BigAutoField(primary_key=True)
    profilename = models.CharField(max_length=255)
    profilelastname = models.CharField(max_length=255)
    profilenumberphone = models.CharField(unique=True, max_length=15, blank=True, null=True)
    profileaccountid = models.OneToOneField(Accounts, models.DO_NOTHING, db_column='profileaccountid', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ProfileAccounts'


class Transactions(models.Model):
    transactionid = models.BigAutoField(primary_key=True)
    transactionamount = models.BigIntegerField()
    transactiondate = models.TimeField()
    transactionreceiver = models.ForeignKey(Accounts, models.DO_NOTHING, db_column='transactionreceiver')
    transactiontransmitter = models.ForeignKey(Accounts, models.DO_NOTHING, db_column='transactiontransmitter', related_name='transactions_transactiontransmitter_set')

    class Meta:
        managed = False
        db_table = 'Transactions'


class Wallet(models.Model):
    walletid = models.BigAutoField(primary_key=True)
    walletbalance = models.BigIntegerField()
    walletaccountsid = models.OneToOneField(Accounts, models.DO_NOTHING, db_column='walletaccountsid')
    walletcoinsid = models.OneToOneField('Walletcoins', models.DO_NOTHING, db_column='walletcoinsid')

    class Meta:
        managed = False
        db_table = 'Wallet'


class Walletcoins(models.Model):
    walletcoinid = models.BigAutoField(primary_key=True)
    walletcoinquantity = models.BigIntegerField()
    walletcoinwalletid = models.OneToOneField(Wallet, models.DO_NOTHING, db_column='walletcoinwalletid')

    class Meta:
        managed = False
        db_table = 'WalletCoins'