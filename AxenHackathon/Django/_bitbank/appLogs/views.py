from django.shortcuts import render, get_object_or_404
from .models import Auditlog
from appAccounts.models import Account

# Create your views here.
def ViewNotificationList(request, AccountUsername):
    user = get_object_or_404(Account, AccountUsername=AccountUsername)
    notifications = Auditlog.objects.all()
    return render(request, 'notifications/notifications_list.html', {'logs':notifications, 'user':user})

def ViewNotification(request, AuditlogID):
    log = get_object_or_404(Auditlog, AuditlogID=AuditlogID)
    return render(request, 'notifications/notification.html', {'log':log})