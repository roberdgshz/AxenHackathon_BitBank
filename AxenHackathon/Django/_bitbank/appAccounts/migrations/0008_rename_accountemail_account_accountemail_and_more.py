# Generated by Django 5.0 on 2025-01-11 18:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appAccounts', '0007_rename_accountemail_account_accountemail_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='account',
            old_name='AccountEmail',
            new_name='accountemail',
        ),
        migrations.RenameField(
            model_name='account',
            old_name='AccountID',
            new_name='accountid',
        ),
        migrations.RenameField(
            model_name='account',
            old_name='AccountNip',
            new_name='accountnip',
        ),
        migrations.RenameField(
            model_name='account',
            old_name='AccountPassword',
            new_name='accountpassword',
        ),
        migrations.RenameField(
            model_name='account',
            old_name='AccountUsername',
            new_name='accountusername',
        ),
    ]
