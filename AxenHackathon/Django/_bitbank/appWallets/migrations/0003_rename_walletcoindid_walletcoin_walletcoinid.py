# Generated by Django 5.0 on 2024-12-29 21:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appWallets', '0002_rename_walletcoins_walletcoin'),
    ]

    operations = [
        migrations.RenameField(
            model_name='walletcoin',
            old_name='WalletCoindID',
            new_name='WalletCoinID',
        ),
    ]
