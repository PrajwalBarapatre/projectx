from django.urls import path, re_path
from . import views

urlpatterns = [
    re_path(r'^business_sector', views.business_sector, name="business_sector"),  
    re_path(r'^get_sub_sector', views.get_sub_sector, name="get_sub_sector"),  
    re_path(r'^get_code_data', views.codedata, name="get_code_data"),  
    re_path(r'^get_currency_data', views.currencydata, name="cuurecydata"), 
    re_path(r'^session_storage', views.session_storage, name="session_storage"), 
]
