from django.urls import path
from .views import *

urlpatterns = [
    path('notification/<int:id>', ViewNotification, name="notification"),
    path('notification_list/<str:user>', ViewNotificationList, name="notification_list"),
]