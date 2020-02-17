from django.db import models
from datetime import datetime
from phonenumber_field.modelfields import PhoneNumberField
from django.core.validators import MaxValueValidator

from django.core.validators import RegexValidator
from django.utils import timezone

class Advisor(models.Model):
    advisor_id = models.UUIDField(primary_key=True)
    first_name = models.CharField(max_length=25)
    middle_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    country_code_primary = models.CharField(max_length=255, default="+91")
    phone_number_primary = models.CharField(max_length=15)
    email_adress = models.EmailField()
    about_seller = models.TextField()
    website = models.URLField(max_length=100, blank=True, null=True)
    portfolio_website = models.URLField(max_length=100, blank=True, null=True)
    professional_link = models.URLField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(default=timezone.now, blank=True)
    album_id = models.IntegerField(blank=True, null=True)
    type = models.CharField(max_length=100, blank=True, null=True)
    title = models.CharField(max_length=255)
    currency = models.CharField(max_length=255, blank=True, null=True)
    trial = models.BooleanField(default=True)
    # usd_askprice = models.DecimalField(max_digits=22, decimal_places=16, null=True, blank=True)


class BusinessAdvisor(models.Model):
    business_id = models.UUIDField(primary_key=True)
    advisor = models.OneToOneField(Advisor, blank=True, null=True, on_delete=models.CASCADE)
    type = models.CharField(max_length=100, blank=True, null=True)
    category1 = models.CharField(max_length=255, blank=True)
    sub_category1 = models.CharField(max_length=255, blank=True)
    category2 = models.CharField(max_length=255, blank=True)
    sub_category2 = models.CharField(max_length=255, blank=True)
    category3 = models.CharField(max_length=255, blank=True)
    sub_category3 = models.CharField(max_length=255, blank=True)
    skill1 = models.CharField(max_length=2000, blank=True)
    skill2 = models.CharField(max_length=255, blank=True)
    skill3 = models.CharField(max_length=255, blank=True)
    language= models.CharField(max_length=2000, blank=True)
    total_advised=models.IntegerField(blank=True, null=True)
    city1 = models.CharField(max_length=255, blank=True)
    state1 = models.CharField(max_length=255, blank=True)
    country1 = models.CharField(max_length=255, blank=True)
    city2 = models.CharField(max_length=255, blank=True)
    state2 = models.CharField(max_length=255, blank=True)
    country2 = models.CharField(max_length=255, blank=True)
    city3 = models.CharField(max_length=255, blank=True)
    state3 = models.CharField(max_length=255, blank=True)
    country3 = models.CharField(max_length=255, blank=True)
    address_line1 = models.CharField(max_length=256, blank=True)
    address_line2 = models.CharField(max_length=256, blank=True)
    address_line3 = models.CharField(max_length=256, blank=True)
    about = models.TextField()
    years_exp = models.IntegerField(blank=True, null=True)
    hour_fee = models.IntegerField(blank=True, null=True)
    hour_fee_usd = models.DecimalField(max_digits=30, decimal_places=4, null=True, blank=True)
    about_seller = models.TextField()
    all_state = models.CharField(max_length=255, blank=True, null=True)
    all_city = models.CharField(max_length=255, blank=True, null=True)
    all_country = models.CharField(max_length=255, blank=True, null=True)
    all_category = models.CharField(max_length=255, blank=True, null=True)
    all_sub_category = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.advisor.first_name

    def save(self, *args, **kwargs):
        self.type = self.advisor.type
        self.about_seller=self.advisor.about_seller
        self.all_city = '' + str(self.city1) + '__' + str(self.city2) + '__' + str(self.city3)
        self.all_state = '' + str(self.state1) + '__' + str(self.state2) + '__' + str(self.state3)
        self.all_country = '' + str(self.country1) + '__' + str(self.country2) + '__' + str(self.country3)
        self.all_category = '' + str(self.category1) + '__' + str(self.category2) + '__' + str(self.category3)
        self.all_sub_category = '' + str(self.sub_category1) + '__' + str(self.sub_category2) + '__' + str(
            self.sub_category3)
        super(BusinessAdvisor, self).save(*args, **kwargs)


class StartupAdvisor(models.Model):
    startup_id = models.UUIDField(primary_key=True)
    advisor = models.OneToOneField(Advisor, blank=True, null=True, on_delete=models.CASCADE)
    type = models.CharField(max_length=100, blank=True, null=True)
    category1 = models.CharField(max_length=255, blank=True)
    sub_category1 = models.CharField(max_length=255, blank=True)
    category2 = models.CharField(max_length=255, blank=True)
    sub_category2 = models.CharField(max_length=255, blank=True)
    category3 = models.CharField(max_length=255, blank=True)
    sub_category3 = models.CharField(max_length=255, blank=True)
    skill1 = models.CharField(max_length=2000, blank=True)
    skill2 = models.CharField(max_length=255, blank=True)
    skill3 = models.CharField(max_length=255, blank=True)
    language= models.CharField(max_length=2000, blank=True)
    total_advised=models.IntegerField(blank=True, null=True)
    city1 = models.CharField(max_length=255, blank=True)
    state1 = models.CharField(max_length=255, blank=True)
    country1 = models.CharField(max_length=255, blank=True)
    city2 = models.CharField(max_length=255, blank=True)
    state2 = models.CharField(max_length=255, blank=True)
    country2 = models.CharField(max_length=255, blank=True)
    city3 = models.CharField(max_length=255, blank=True)
    state3 = models.CharField(max_length=255, blank=True)
    country3 = models.CharField(max_length=255, blank=True)
    address_line1 = models.CharField(max_length=256, blank=True)
    address_line2 = models.CharField(max_length=256, blank=True)
    address_line3 = models.CharField(max_length=256, blank=True)
    about = models.TextField()
    years_exp = models.IntegerField(blank=True, null=True)
    hour_fee = models.IntegerField(blank=True, null=True)
    hour_fee_usd = models.DecimalField(max_digits=30, decimal_places=4, null=True, blank=True)
    about_seller = models.TextField()
    all_state = models.CharField(max_length=255, blank=True, null=True)
    all_city = models.CharField(max_length=255, blank=True, null=True)
    all_country = models.CharField(max_length=255, blank=True, null=True)
    all_category = models.CharField(max_length=255, blank=True, null=True)
    all_sub_category = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.advisor.first_name

    def save(self, *args, **kwargs):
        self.type = self.advisor.type
        self.about_seller = self.advisor.about_seller
        self.all_city = '' + str(self.city1) + '__' + str(self.city2) + '__' + str(self.city3)
        self.all_state = '' + str(self.state1) + '__' + str(self.state2) + '__' + str(self.state3)
        self.all_country = '' + str(self.country1) + '__' + str(self.country2) + '__' + str(self.country3)
        self.all_category = '' + str(self.category1) + '__' + str(self.category2) + '__' + str(self.category3)
        self.all_sub_category = '' + str(self.sub_category1) + '__' + str(self.sub_category2) + '__' + str(
            self.sub_category3)
        super(StartupAdvisor, self).save(*args, **kwargs)
