from django.urls import path
from .views import *

urlpatterns = [
    path('notification/<int:AuditlogID>', ViewNotification, name="notification"),
    path('notification_list/<str:AccountUsername>', ViewNotificationList, name="notification_list"),
]