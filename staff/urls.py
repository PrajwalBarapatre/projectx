from django.urls import path,  include
from staff import views, listings
from chat.views import staff_whatsapp

urlpatterns = [
    path('newtask', views.create_Task, name='staff-home'),
    path('whatsapp', staff_whatsapp, name='staff-whatsapp'),
    path('generate_otps', views.createRegTask, name='generate-otps'),
    path('regtask', views.createRegUser, name='client-reg'),
    path('business_task/<task_hash>', listings.Business_task, name='business_task'),
    path('asset_task/<task_hash>', listings.Asset_task, name='asset_task'),
    path('loan_task/<task_hash>', listings.Loan_task, name='loan_task'),
    path('equity_task/<task_hash>', listings.Equity_task, name='equity_task'),
    path('startup_task/<task_hash>', listings.Startup_task, name='startup_task'),
    path('ipcode_task/<task_hash>', listings.Ipcode_task, name='ipcode_task'),
    path('application_task/<task_hash>', listings.App_task, name='app_task'),
    path('franchise_task/<task_hash>', listings.Franchise_task, name='franchise_task'),
    path('supplier_task/<task_hash>', listings.Supplier_task, name='supplier_task'),


]
