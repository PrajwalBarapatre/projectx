from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone
from seller1.models import Seller1
from advisor.models import Advisor
from investor.models import Investor
from user_seller.models import Sell, Advise, Invest
from chat.models import Chat
from projectx import settings
# from attempts.models import Attempt


class Feedback(models.Model):
    feedback_id = models.AutoField(primary_key=True)
    email = models.EmailField()
    question = models.TextField()
    created_at = models.DateTimeField(default=timezone.now, editable=False)


class Notification(models.Model):
    notif_id = models.AutoField(primary_key=True)
    notif_type = models.CharField(max_length=255)
    notif_statement = models.CharField(max_length=255)
    notif_on = models.CharField(max_length=255, blank=True, null=True)
    notif_on_id = models.CharField(max_length=255, blank=True, null=True)
    notif_seen = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=timezone.now, editable=False)

class Search_log(models.Model):
    slog_id = models.AutoField(primary_key=True)
    city = models.CharField(max_length=255, blank=True, null=True)
    state = models.CharField(max_length=255, blank=True, null=True)
    country = models.CharField(max_length=255, blank=True, null=True)
    base_type = models.CharField(max_length=255, blank=True, null=True)
    type = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(default=timezone.now, editable=False)

class View_log(models.Model):
    vlog_id = models.AutoField(primary_key=True)
    base_type = models.CharField(max_length=255, blank=True, null=True)
    type = models.CharField(max_length=255, blank=True, null=True)
    category = models.CharField(max_length=255, blank=True, null=True)
    time_spent = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(default=timezone.now, editable=False)
    id = models.CharField(max_length=255, blank=True, null=True)

class Profile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=255, blank=True, null=True)
    last_name = models.CharField(max_length=255, blank=True, null=True)
    photo = models.FileField(upload_to='files/', blank=True, null=True, default='files/advisor-img2.png')
    photo_url =models.CharField(max_length=255, blank=True, null=True)
    contact_number = models.CharField(max_length=10, blank=True, null=True)
    country = models.CharField(max_length=256, blank=True, null=True)
    region = models.CharField(max_length=256, blank=True, null=True)
    city = models.CharField(max_length=256, blank=True, null=True)
    lat = models.DecimalField(max_digits=22, decimal_places=16, null=True, blank=True)
    lngt = models.DecimalField(max_digits=22, decimal_places=16, null=True, blank=True)
    address_line = models.CharField(max_length=255)
    notifs = models.ManyToManyField(Notification, blank=True, null=True)
    about_me = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(default=timezone.now, editable=False)
    status = models.BooleanField(default=False)
    sell_type = models.ManyToManyField(Seller1, related_name='profile_from_seller', blank=True)
    advise_type = models.ManyToManyField(Advisor, related_name='profile_from_advisor', blank=True)
    invest_type = models.OneToOneField(Investor, related_name='profile_from_investor', blank=True, null=True, on_delete=models.SET_NULL)
    user_sell = models.ManyToManyField(Sell, blank=True)
    user_advise = models.ManyToManyField(Advise, blank=True)
    user_invest = models.ManyToManyField(Invest, blank=True)
    curr_chat = models.ForeignKey(Chat, blank=True, null=True, on_delete=models.SET_NULL)
    just_sell = models.ManyToManyField(Seller1, related_name='profile_from_jseller', blank=True)
    just_advise = models.ManyToManyField(Advisor, related_name='profile_from_jadvisor', blank=True)
    just_invest = models.ManyToManyField(Investor, related_name='profile_from_jinvestor', blank=True)
    investors_type = models.ManyToManyField(Investor, related_name='related_investor', blank=True)
    social = models.BooleanField(default=False)
    premium = models.BooleanField(default=False)
    trial = models.BooleanField(default=True)
    otp = models.CharField(blank=True, null=True, max_length=255)
    # active = models.BooleanField(default=True)
    # otp_valid = models.BooleanField(default=False)
    searches = models.ManyToManyField(Search_log, blank=True, null=True)
    views = models.ManyToManyField(View_log, blank=True, null=True)

    # class Paypal_Order(models.Model):
    #     order_id = models.AutoField(primary_key=True)
    #     user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    #     subcription_plan = models.CharField(max_length=255, blank=True, null=True)
    #     listing_type = models.CharField(max_length=255, blank=True, null=True)
    #     listing_id = models.CharField(max_length=255, blank=True, null=True)
    #     currency_code = models.CharField(max_length=255, blank=True, null=True)
    #     price = models.CharField(max_length=255, blank=True, null=True)
    #     order_time = models.DateTimeField(default=timezone.now, editable=False)
    #     trial = models.BooleanField(default=False)
    #     duration = models.IntegerField(blank=True, null=True)  
    
    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()