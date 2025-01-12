from django.urls import path
from .views import *

urlpatterns = [
    path('deposit/', ViewTransactionDeposit.as_view(), name="transaction_deposit"),
    path('menu/', ViewTransactionMenu.as_view(), name="transaction_menu"),
    path('receive/', ViewTransactionReceive.as_view(), name="transaction_receive"),
    path('history/<str:user>', ViewTransactionHistory, name="transaction_history"),
    path('info/<int:id>', ViewTransactionInfo, name="transaction_info"),
]