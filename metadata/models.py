from django.db import models
from datetime import datetime

# Create your models here.
class BusinessSectors(models.Model):
    sectors = models.CharField(max_length=255, blank= True, default = "")
    sub_sectors = models.CharField(max_length=255, blank= True, default = "")
#    created_at = models.DateTimeField(default = datetime.now, blank = True)

class codes(models.Model):
#    country = models.CharField(max_length=255, blank= True, default = "")
    dialing = models.CharField(max_length=255, blank= True, default = "")
    code = models.CharField(max_length=255, blank= True, default = "")
    iso= models.CharField(max_length=255, blank= True, default = "")

#    created_at = models.DateTimeField(default = datetime.now, blank = True)

class advisor(models.Model):
    types = models.CharField(max_length=255, blank= True, default = "")
#    created_at = models.DateTimeField(default = datetime.now, blank = True)

    
class company(models.Model):
    types = models.CharField(max_length=255, blank= True, default = "")
#    created_at = models.DateTimeField(default = datetime.now, blank = True)


class years(models.Model):
    code = models.IntegerField(blank= True, default = 0)

class currency(models.Model):
    country = models.CharField(max_length=255, blank= True, default = "")
    usdconv = models.DecimalField(max_digits=22, decimal_places=16, null=True, blank=True)
