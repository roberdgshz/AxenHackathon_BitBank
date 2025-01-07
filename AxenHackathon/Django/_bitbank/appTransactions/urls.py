from django.urls import path
from .views import *

urlpatterns = [
    path('deposit/', ViewTransactionDeposit.as_view(), name="transaction_deposit"),
    path('history/', ViewTransactionHistory.as_view(), name="transaction_history"),
    path('info/', ViewTransactionInfo.as_view(), name="transaction_info"),
    path('menu/', ViewTransactionMenu.as_view(), name="transaction_menu"),
    path('receive/', ViewTransactionReceive.as_view(), name="transaction_receive"),
]