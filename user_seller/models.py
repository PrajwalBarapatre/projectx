from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone
from seller1.models import Seller1
from investor.models import Investor
from advisor.models import Advisor

class Sell(models.Model):
    sell_id = models.AutoField(primary_key=True)
    seller = models.OneToOneField(Seller1, blank=True, null=True, on_delete=models.CASCADE)
    inst_investors = models.ManyToManyField(Investor, related_name='invest_sell_for_sell', blank=True)
    inst_advisor = models.ManyToManyField(Advisor, related_name='advise_sell_for_sell', blank=True)
    cart_investor = models.ManyToManyField(Investor, related_name='invest_cart_for_sell', blank=True)
    cart_advisor = models.ManyToManyField(Advisor, related_name='advise_cart_for_sell', blank=True)
    type = models.CharField(max_length=255, blank=True, null=True)
    cart_sellers = models.ManyToManyField(Seller1, blank=True, null=True, related_name='inst_suppliers')
    inst_sellers = models.ManyToManyField(Seller1, blank=True, null=True, related_name='cart_suppliers')
    cart_suppliers = models.ManyToManyField(Seller1, blank=True, null=True, related_name='inst_sells')
    inst_suppliers = models.ManyToManyField(Seller1, blank=True, null=True, related_name='cart_sells')
    is_mobile = models.BooleanField(default=False, blank=True, null=True)

    def __str__(self):
        return self.seller.title

    def save(self, *args, **kwargs):
        self.type = self.seller.type
        super(Sell, self).save(*args, **kwargs)

class Invest(models.Model):
    invest_id = models.AutoField(primary_key=True)
    investor = models.OneToOneField(Investor, blank=True, null=True, on_delete=models.CASCADE)
    inst_seller = models.ManyToManyField(Seller1, related_name='invest_sell_for_invest', blank=True)
    inst_advisor = models.ManyToManyField(Advisor, related_name='advise_sell_for_invest', blank=True)
    cart_seller = models.ManyToManyField(Seller1, related_name='invest_cart_for_invest', blank=True)
    cart_advisor = models.ManyToManyField(Advisor, related_name='advise_cart_for_invest', blank=True)
    type = models.CharField(max_length=255, blank=True, null=True)
    is_mobile = models.BooleanField(default=False, blank=True, null=True)

    def __str__(self):
        return self.investor.first_name

    def save(self, *args, **kwargs):
        self.type = self.investor.type
        super(Invest, self).save(*args, **kwargs)

class Advise(models.Model):
    advise_id = models.AutoField(primary_key=True)
    advisor = models.OneToOneField(Advisor, blank=True, null=True, on_delete=models.CASCADE)
    inst_seller = models.ManyToManyField(Seller1, related_name='invest_sell_for_advise', blank=True)
    inst_invest = models.ManyToManyField(Investor, related_name='advise_sell_for_advise', blank=True)
    cart_seller = models.ManyToManyField(Seller1, related_name='invest_cart_for_advise', blank=True)
    cart_invest = models.ManyToManyField(Investor, related_name='advise_cart_for_advise', blank=True)
    type = models.CharField(max_length=255, blank=True, null=True)
    is_mobile = models.BooleanField(default=False, blank=True, null=True)

    def __str__(self):
        return self.advisor.first_name

    def save(self, *args, **kwargs):
        self.type = self.advisor.type
        super(Advise, self).save(*args, **kwargs)