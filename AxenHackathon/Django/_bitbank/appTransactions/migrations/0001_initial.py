# Generated by Django 5.1.4 on 2025-01-04 17:50

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('TransactionID', models.BigAutoField(primary_key=True, serialize=False)),
                ('TransactionAmount', models.BigIntegerField()),
                ('TransactionDate', models.DateTimeField()),
                ('TransactionReceiver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='receiver', to=settings.AUTH_USER_MODEL)),
                ('TransactionTransmitter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='transmitter', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
