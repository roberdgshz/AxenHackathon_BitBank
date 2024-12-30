from django.contrib import admin

# Register your models here.
from .models import (Accounts, Auditlogs, Coins, Profileaccounts, Transactions, Wallet, Walletcoins)

# Registrar los modelos
admin.site.register(Accounts)
admin.site.register(Auditlogs)
admin.site.register(Coins)
admin.site.register(Profileaccounts)
admin.site.register(Transactions)
admin.site.register(Wallet)
admin.site.register(Walletcoins)
