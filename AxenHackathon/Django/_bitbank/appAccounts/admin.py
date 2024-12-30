from django.contrib import admin
from .models import *
# Register your models here.
<<<<<<< HEAD

admin.site.register(Account)
admin.site.register(ProfileAccount)
=======
from .models import (Accounts, Auditlogs, Coins, Profileaccounts, Transactions, Wallet, Walletcoins)

# Registrar los modelos
admin.site.register(Accounts)
admin.site.register(Auditlogs)
admin.site.register(Coins)
admin.site.register(Profileaccounts)
admin.site.register(Transactions)
admin.site.register(Wallet)
admin.site.register(Walletcoins)
>>>>>>> 799dbc47461350514c047e96c2008c2519d0ba25
