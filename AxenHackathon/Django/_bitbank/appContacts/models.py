from django.db import models
from django.conf import settings

class Contact(models.Model):
    contactid = models.BigAutoField(primary_key=True)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='owned_contacts')
    contact_user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='in_contacts')
    nickname = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        db_table = "contact"
        unique_together = ['owner', 'contact_user']

    def __str__(self):
        return f"{self.owner.accountusername}'s contact: {self.nickname or self.contact_user.accountusername}"