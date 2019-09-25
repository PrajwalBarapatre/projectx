from django.contrib import admin
from .models import Seller1

class seller1Admin(admin.ModelAdmin):
    pass


admin.site.register(Seller1, seller1Admin)

