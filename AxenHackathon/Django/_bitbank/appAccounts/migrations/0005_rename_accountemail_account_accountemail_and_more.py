# Generated by Django 5.0 on 2025-01-11 18:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appAccounts', '0004_rename_accountemail_account_accountemail_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='account',
            old_name='accountemail',
            new_name='AccountEmail',
        ),
        migrations.RenameField(
            model_name='account',
            old_name='accountid',
            new_name='AccountID',
        ),
        migrations.RenameField(
            model_name='account',
            old_name='accountnip',
            new_name='AccountNip',
        ),
        migrations.RenameField(
            model_name='account',
            old_name='accountpassword',
            new_name='AccountPassword',
        ),
        migrations.RenameField(
            model_name='account',
            old_name='accountusername',
            new_name='AccountUsername',
        ),
    ]