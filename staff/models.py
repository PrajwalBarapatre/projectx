from django.db import models
from django.contrib.auth.models import User
from user_seller.models import Sell, Advise, Invest
from django.utils import timezone
import uuid
from datetime import datetime, timedelta
# Create your models here.

class Task(models.Model):
    task_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name='staff_task')
    client = models.ForeignKey(User, blank=True, null=True, related_name='client_task', on_delete=models.CASCADE)
    client_email = models.EmailField(blank=True, null=True)
    listing_type = models.CharField(max_length=255, blank=True, null=True)
    lead_type = models.CharField(max_length=255, blank=True, null=True)
    sell = models.OneToOneField(Sell, blank=True, null=True, on_delete=models.CASCADE)
    advise = models.OneToOneField(Advise, blank=True, null=True, on_delete=models.CASCADE)
    invest = models.OneToOneField(Invest, blank=True, null=True, on_delete=models.CASCADE)
    task_hash = models.CharField(blank=False, max_length=255, unique=True)
    task_enc = models.CharField(blank=False, max_length=255, unique=True)
    expires = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(default=timezone.now, editable=False)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.client.profile.first_name

    def save(self, *args, **kwargs):

        super(Task, self).save(*args, **kwargs)