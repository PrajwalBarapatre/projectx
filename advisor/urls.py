from django.urls import path, re_path
from . import views
from django.conf.urls import url
from django.urls import path

urlpatterns = [
    path('user_detail/<business_id>', views.detail_advise_type, name='advisor-user-detail'),
    path('all_detail/<business_id>', views.just_advise_type, name='advisor-all-detail'),
    url('ajax/update/files/', views.UpdateFiles, name='investor-update-files'),
    path('business/delete/<business_id>', views.AdvisorBusiDelete, name='busi-delete'),
    path('startup/delete/<business_id>', views.AdvisorStartupDelete, name='startup-delete'),
    path('business', views.advisor_busi, name='business'),
    path('startup', views.advisor_startup, name='startup'),
    path('business_update/<business_id>', views.BusinessUpdate, name='business-update'),
    path('startup_update/<business_id>', views.StartupUpdate, name='startup-update'),
    url('ajax/validate/$', views.validate, name='advisor-validate'),
    url('ajax/validate/busi/', views.validate_busi, name='business-validate-busi'),
    url('ajax/validate/startup/', views.validate_startup, name='business-validate-startup'),
]