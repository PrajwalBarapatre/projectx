from django.db import models
# from django.contrib.gis.db import models as gmodels
# from django.contrib.gis.geos import Point
from datetime import datetime
from phonenumber_field.modelfields import PhoneNumberField
from django.core.validators import MaxValueValidator
from django.contrib.auth.models import User

from django.core.validators import RegexValidator
from django.utils import timezone

SELL_1 = 'Sell Business'
SELL_2 = 'Sell Assets in Business'
SELL_3 = 'Sell Stake in Business'
SELL_4 = 'Raise Loan for Business'
Here_to_sell = (
	(SELL_1, 'Business'),
	(SELL_2, 'Asset'),
	(SELL_3, 'Equity'),
	(SELL_4, 'Loan')
)

class Seller1(models.Model):
    business_id = models.AutoField(primary_key=True, blank=True)
    first_name = models.CharField(max_length=25)
    middle_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    country_code_primary = models.CharField(max_length=255, default = "+91")
    phone_number_primary = models.CharField(max_length=15)
    email_adress = models.EmailField(max_length=40)
    about_seller = models.TextField(blank=True, null=True)
    # seller_purpose = models.TextField(blank=True, default="0", max_length=255)
    created_at = models.DateTimeField(default = timezone.now, blank = True)
    #flags
    completed = models.IntegerField(default=0)
   # phone_verified = models.IntegerField(default=0)
    #page2 models
    category1 = models.CharField(max_length=255, blank= True)
    category2 = models.CharField(max_length=255, blank= True)
    business_type = models.CharField(max_length=255,  blank=True)
    name = models.CharField(max_length=40, default='')
    title = models.CharField(max_length=255)
    country = models.CharField(max_length=256,blank=True, null=True)
    region = models.CharField(max_length=256,blank=True, null=True)
    city = models.CharField(max_length=256,blank=True, null=True)
    adress = models.TextField(blank=True, max_length=255)
    lat = models.DecimalField(max_digits=22, decimal_places=16, null=True, blank=True)
    lngt = models.DecimalField(max_digits=22, decimal_places=16, null=True, blank=True)
    address_line = models.CharField(max_length=255)
    currency = models.CharField(max_length=255, blank=True, null=True)
    # geo_cord = gmodels.PointField(blank = True, null=True)
    album_id = models.IntegerField(blank=True, null=True)
    type = models.CharField(max_length=100, blank=True, null=True)

    viewers = models.ManyToManyField(User, blank=True, null=True)

    # def save(self, *args, **kwargs):
    #     if(self.lat and self.lngt):
    #         self.geo_cord = Point(self.lngt, self.lat)
    #     super(Seller1, self).save(*args, **kwargs)

class Ablumfiles(models.Model):
    seller_id = models.IntegerField(blank=True, null=True)
    file_name = models.CharField(max_length=100)

class SellBusiness(models.Model):
    seller = models.OneToOneField(Seller1, blank=True, null=True, on_delete=models.CASCADE)
    business_id = models.AutoField(primary_key=True)
    type = models.CharField(max_length=100, blank=True, null=True)
    about = models.TextField()
    asking_price = models.IntegerField()
    asking_price_usd = models.DecimalField(max_digits=30, decimal_places=4, null=True, blank=True)
    year_established = models.IntegerField()
    reason_selling = models.TextField()
    website = models.URLField(max_length=500, blank=True, null=True)

    def __str__(self):
        return self.seller.title

    def save(self, *args, **kwargs):
        self.type = self.seller.type
        super(SellBusiness, self).save(*args, **kwargs)

class SellAsset(models.Model):
    asset_id = models.AutoField(primary_key=True)
    seller = models.OneToOneField(Seller1, blank=True, null=True, on_delete=models.CASCADE)
    type = models.CharField(max_length=100, blank=True, null=True)
    asset_type = models.CharField(blank=True, max_length=255)
    about_asset = models.TextField(blank=True, max_length=255)
    asking_price = models.IntegerField(blank=True)
    asking_price_usd = models.DecimalField(max_digits=30, decimal_places=4, null=True, blank=True)
    purchase_price = models.IntegerField(blank=True)
    purchase_price_usd = models.DecimalField(max_digits=30, decimal_places=4, null=True, blank=True)
    purchase_year = models.IntegerField(blank=True)
    reason_selling = models.TextField(blank=True, max_length=255)

    def __str__(self):
        return self.seller.title

    def save(self, *args, **kwargs):
        self.type = self.seller.type
        super(SellAsset, self).save(*args, **kwargs)

class RaiseLoan(models.Model):
    loan_id = models.AutoField(primary_key=True)
    seller = models.OneToOneField(Seller1, blank=True, null=True, on_delete=models.CASCADE)
    type = models.CharField(max_length=100, blank=True, null=True)
    about_business = models.TextField(blank=True, max_length=255)
    loan_amount = models.IntegerField(blank=True,null=True)
    loan_amount_usd = models.DecimalField(max_digits=30, decimal_places=4, null=True, blank=True)
    sought_interest = models.DecimalField(blank=True, decimal_places=20, max_digits=30)
    year_established = models.IntegerField(blank=True)
    reason_loan = models.TextField(blank=True, max_length=255)
    website = models.URLField(max_length=500, blank=True, null=True)

    def __str__(self):
        return self.seller.title

    def save(self, *args, **kwargs):
        self.type = self.seller.type
        super(RaiseLoan, self).save(*args, **kwargs)

class SellEquity(models.Model):
    equity_id = models.AutoField(primary_key=True)
    seller = models.OneToOneField(Seller1, blank=True, null=True, on_delete=models.CASCADE)
    type = models.CharField(max_length=100, blank=True, null=True)
    about_business = models.TextField(blank=True, max_length=255)
    stake = models.DecimalField(blank=True, decimal_places=20, max_digits=30)
    asking_price = models.IntegerField(blank=True)
    asking_price_usd = models.DecimalField(max_digits=30, decimal_places=4, null=True, blank=True)
    year = models.IntegerField(blank=True)
    reason = models.TextField(blank=True, max_length=255)
    website = models.URLField(max_length=500, blank=True, null=True)

    def __str__(self):
        return self.seller.title

    def save(self, *args, **kwargs):
        self.type = self.seller.type
        super(SellEquity, self).save(*args, **kwargs)


class RevenueModel(models.Model):
    revenue_id = models.AutoField(primary_key=True)
    rev_year = models.IntegerField()
    year_16 = models.IntegerField(blank=True, default=0)
    year_15 = models.IntegerField(blank=True, default=0)
    year_14 = models.IntegerField(blank=True, default=0)
    year_13 = models.IntegerField(blank=True, default=0)
    year_17 = models.IntegerField(blank=True, default=0)
    no_emp = models.IntegerField(blank=True, default=0)
    cp_emp = models.IntegerField(blank=True, default=0)
    rev_year_usd = models.DecimalField(max_digits=30, decimal_places=4, null=True, blank=True)
    year_16_usd = models.DecimalField(max_digits=30, decimal_places=4, null=True, blank=True)
    year_15_usd = models.DecimalField(max_digits=30, decimal_places=4, null=True, blank=True)
    year_14_usd = models.DecimalField(max_digits=30, decimal_places=4, null=True, blank=True)
    year_13_usd = models.DecimalField(max_digits=30, decimal_places=4, null=True, blank=True)
    year_17_usd = models.DecimalField(max_digits=30, decimal_places=4, null=True, blank=True)
    cp_emp_usd = models.DecimalField(max_digits=30, decimal_places=4, null=True, blank=True)
    seller = models.OneToOneField(Seller1, blank = True, null = True, on_delete = models.CASCADE)

class SellStartup(models.Model):
    startup_id = models.AutoField(primary_key=True)
    seller = models.OneToOneField(Seller1, blank=True, null=True, on_delete=models.CASCADE)
    type = models.CharField(max_length=100, blank=True, null=True)
    about = models.TextField()
    sought_equity = models.DecimalField(blank=True, null=True, decimal_places=20, max_digits=30)
    asking_price = models.IntegerField()
    asking_price_usd = models.DecimalField(max_digits=30, decimal_places=4, null=True, blank=True)
    revenue_growth = models.DecimalField(blank=True, null=True, decimal_places=20, max_digits=30)
    year_established = models.IntegerField()
    reason_selling = models.TextField()
    website = models.URLField(max_length=500, blank=True, null=True)


    def __str__(self):
        return self.seller.title

    def save(self, *args, **kwargs):
        self.type = self.seller.type
        super(SellStartup, self).save(*args, **kwargs)


class SellApp(models.Model):
    app_id = models.AutoField(primary_key=True)
    seller = models.OneToOneField(Seller1, blank=True, null=True, on_delete=models.CASCADE)
    type = models.CharField(max_length=100, blank=True, null=True)
    about = models.TextField()
    startup_type = models.CharField(max_length=255, blank=True)
    email_app = models.EmailField(max_length=255, blank=True,default = "nothing@gmail.com")
    asking_price = models.IntegerField()
    asking_price_usd = models.DecimalField(max_digits=30, decimal_places=4, null=True, blank=True)
    website = models.URLField(max_length=500, blank=True, null=True)
    monitization_method = models.CharField(max_length=255, blank=True)
    average_monthly_revenue = models.IntegerField()
    average_monthly_expense = models.IntegerField()
    average_monthly_revenue_usd = models.DecimalField(max_digits=30, decimal_places=4, null=True, blank=True)
    average_monthly_expense_usd = models.DecimalField(max_digits=30, decimal_places=4, null=True, blank=True)
    date_established = models.DateField()
    average_monthly_downloads = models.IntegerField()
    platform_used=models.CharField(max_length=500, blank=True)
    y1_views=models.IntegerField(blank=True, null=True,default = 0)
    y2_views=models.IntegerField(blank=True, null=True,default = 0)
    y3_views=models.IntegerField(blank=True, null=True,default = 0)
    y1_users=models.IntegerField(blank=True, null=True,default = 0)
    y2_users=models.IntegerField(blank=True, null=True,default = 0)
    y3_users=models.IntegerField(blank=True, null=True,default = 0)


    def __str__(self):
        return self.seller.title

    def save(self, *args, **kwargs):
        self.type = self.seller.type
        super(SellApp, self).save(*args, **kwargs)

class SellIpcode(models.Model):
    ipcode_id = models.AutoField(primary_key=True)
    seller = models.OneToOneField(Seller1, blank=True, null=True, on_delete=models.CASCADE)
    type = models.CharField(max_length=100, blank=True, null=True)
    startup_type = models.CharField(max_length=255, blank=True)
    research_title = models.TextField()
    product_type = models.CharField(max_length=255, blank=True)
    about = models.TextField()
    asking_price = models.BigIntegerField()
    asking_price_usd = models.DecimalField(max_digits=30, decimal_places=4, null=True, blank=True)
    website = models.URLField(max_length=500, blank=True, null=True)


    def __str__(self):
        return self.seller.title

    def save(self, *args, **kwargs):
        self.type = self.seller.type
        super(SellIpcode, self).save(*args, **kwargs)


class SellFranchise(models.Model):
    franchise_id = models.AutoField(primary_key=True)
    seller = models.OneToOneField(Seller1, blank=True, null=True, on_delete=models.CASCADE)
    type = models.CharField(max_length=100, blank=True, null=True)
    num_outlets = models.IntegerField(max_length=100, default=1)
    franchise_type = models.CharField(max_length=255, blank=True)
    prod_info = models.TextField()
    looking_for = models.TextField()
    asking_price = models.IntegerField(blank=True, default=0, null=True)
    asking_price_usd = models.DecimalField(max_digits=30, decimal_places=4, null=True, blank=True)
    cap_req = models.IntegerField(blank=True, default=0, null=True)
    exp_ret = models.DecimalField(blank=True, null=True, decimal_places=20, max_digits=30)
    website = models.URLField(max_length=500, blank=True, null=True)

    def __str__(self):
        return self.seller.title

    def save(self, *args, **kwargs):
        self.type = self.seller.type
        super(SellFranchise, self).save(*args, **kwargs)

class Supplier(models.Model):
    supplier_id = models.AutoField(primary_key=True)
    seller = models.OneToOneField(Seller1, blank=True, null=True, on_delete=models.CASCADE)
    type = models.CharField(max_length=100, blank=True, null=True)
    supplier_type = models.CharField(max_length=100, blank=True, null=True)
    prod_info = models.TextField()  
    # looking_for = models.TextField()
    # asking_price = models.IntegerField(blank=True, default=0, null=True)
    exp_ret = models.DecimalField(blank=True, null=True, decimal_places=20, max_digits=30)
    website = models.URLField(max_length=500, blank=True, null=True)

    def __str__(self):
        return self.seller.title

    def save(self, *args, **kwargs):
        self.type = self.seller.type
        super(Supplier, self).save(*args, **kwargs)
