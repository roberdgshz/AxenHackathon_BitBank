from django.urls import path
from .views import *

urlpatterns = [
    path('deposit/<str:user>', ViewTransactionDeposit, name="transaction_deposit"),
    path('menu/', ViewTransactionMenu.as_view(), name="transaction_menu"),
    path('receive/<str:user>', ViewTransactionReceive, name="transaction_receive"),
    path('history/<str:user>', ViewTransactionHistory, name="transaction_history"),
    path('info/<int:id>', ViewTransactionInfo, name="transaction_info"),
    path('receive_generator/', ViewTransactionReceiveGenerator, name="transaction_receive_generator"),
    path('deposit_generator/', ViewTransactionDepositGenerator, name="transaction_deposit_generator"),
]