# Generated by Django 5.0 on 2025-01-02 16:07

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appAccounts', '0001_initial'),
        ('appTransactions', '0002_rename_transactions_transaction'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='TransactionReceiver',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='receiver', to='appAccounts.account'),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='TransactionTransmitter',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='transmitter', to='appAccounts.account'),
        ),
    ]