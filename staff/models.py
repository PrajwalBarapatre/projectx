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

class RegTask(models.Model):
    reg_task_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True, related_name='staff_reg_task')
    client_email = models.EmailField(blank=True, null=True)
    client_phone = models.CharField(max_length=255, blank=True, null=True)
    country_code_primary = models.CharField(max_length=255, default="+91")
    otp_email = models.CharField(max_length=255, blank=True, null=True)
    otp_phone = models.CharField(max_length=255, blank=True, null=True)
    client = models.ForeignKey(User, blank=True, null=True, related_name='client_reg_task', on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now, editable=False)

class EmailModel(models.Model):
    model_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name='user_emails')
    created_at = models.DateTimeField(default=timezone.now, editable=False)

class PhoneModel(models.Model):
    model_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    phone_number = models.CharField(max_length=255, blank=True, null=True)
    country_code_primary = models.CharField(max_length=255, default="+91")
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name='user_phones')
    created_at = models.DateTimeField(default=timezone.now, editable=False)