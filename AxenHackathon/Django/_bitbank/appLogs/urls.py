from django.urls import path
from .views import *

urlpatterns = [
    path('notification/', ViewNotification.as_view(), name="notification"),
    path('notification_list/', ViewNotificationList.as_view(), name="notification_list"),
]