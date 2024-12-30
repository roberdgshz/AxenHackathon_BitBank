from django.db import models
from appAccounts.models import Account

# Create your models here.
class Auditlog(models.Model):
    AuditlogID      = models.BigAutoField(primary_key=True)
    AuditlogAccount = models.OneToOneField(
        Account,
        on_delete=models.CASCADE
    )
    AuditlogDescription = models.TextField()
    AuditlogTime        = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f"{self.AuditlogID}, {self.AuditlogTime}"