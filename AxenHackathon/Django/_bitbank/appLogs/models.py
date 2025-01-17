from django.db import models
from appAccounts.models import Account

# Create your models here.
class AuditType(models.Model):
    auditid   = models.IntegerField(primary_key=True)
    auditname = models.CharField(unique=True, max_length=255)

    class Meta:
        db_table = "audit_type"

    def __str__(self):
        return self.auditname

class Auditlog(models.Model):
    auditlogid        = models.BigAutoField(primary_key=True)
    auditlogdescription = models.TextField()
    auditlogaccountid = models.ForeignKey(
        Account,
        on_delete=models.CASCADE
    )
    auditlogtime        = models.DateTimeField(blank=True, null=True)
    audittypeid = models.ForeignKey(
        AuditType,
        on_delete=models.CASCADE
    )

    class Meta:
        db_table = "auditlog"

    def __str__(self):
        return f"Notification: {self.auditlogid}, time: {self.auditlogtime}, by: {self.auditlogaccountid}"