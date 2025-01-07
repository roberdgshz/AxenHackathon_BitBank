from django.views.generic import TemplateView
from django.shortcuts import render

# Create your views here.
class ViewNotification(TemplateView):
    template_name = 'notifications/notification.html'

class ViewNotificationList(TemplateView):
    template_name = 'notifications/notifications_list.html'