# Generated by Django 5.0 on 2025-01-13 01:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appWallets', '0013_alter_wallet_walletcoinquantity'),
    ]

    operations = [
        migrations.RenameField(
            model_name='wallet',
            old_name='walletcoinQuantity',
            new_name='walletcoinquantity',
        ),
    ]