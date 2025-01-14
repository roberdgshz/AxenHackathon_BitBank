# Generated by Django 5.0 on 2025-01-12 21:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appWallets', '0010_alter_coin_coinvalue'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coin',
            name='coinvalue',
            field=models.DecimalField(decimal_places=20, max_digits=100),
        ),
        migrations.AlterField(
            model_name='wallet',
            name='walletbalance',
            field=models.DecimalField(decimal_places=20, max_digits=100),
        ),
    ]
