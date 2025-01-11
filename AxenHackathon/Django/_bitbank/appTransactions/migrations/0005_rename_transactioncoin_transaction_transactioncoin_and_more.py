# Generated by Django 5.0 on 2025-01-11 21:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appTransactions', '0004_transaction_transactioncoin'),
    ]

    operations = [
        migrations.RenameField(
            model_name='transaction',
            old_name='TransactionCoin',
            new_name='transactioncoin',
        ),
        migrations.RenameField(
            model_name='transaction',
            old_name='TransactionDate',
            new_name='transactiondate',
        ),
        migrations.RenameField(
            model_name='transaction',
            old_name='TransactionID',
            new_name='transactionid',
        ),
        migrations.RenameField(
            model_name='transaction',
            old_name='TransactionReceiver',
            new_name='transactionreceiver',
        ),
        migrations.RenameField(
            model_name='transaction',
            old_name='TransactionTransmitter',
            new_name='transactiontransmitter',
        ),
        migrations.RemoveField(
            model_name='transaction',
            name='TransactionAmount',
        ),
        migrations.AddField(
            model_name='transaction',
            name='transactionamount',
            field=models.DecimalField(decimal_places=50, default=1, max_digits=100),
            preserve_default=False,
        ),
    ]