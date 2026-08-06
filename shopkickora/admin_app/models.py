from django.db import models
# Create your models here.
from django.contrib.auth import get_user_model
User=get_user_model()

class ClientNotification(models.Model):

    customer = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="trs_notifications"
    )

    subject = models.CharField(max_length=255)

    message = models.TextField()

    is_read = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)