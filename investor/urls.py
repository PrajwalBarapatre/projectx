from django.urls import path, re_path
from . import views
from django.conf.urls import url
from django.urls import path

urlpatterns = [
    path('user_detail/<business_id>', views.detail_invest_type, name='investor-user-detail'),
    path('all_detail/<business_id>', views.just_invest_type, name='investor-all-detail'),
    url('ajax/update/files/', views.UpdateFiles, name='investor-update-files'),
    path('individual', views.investor_indiv, name='individual'),
    path('individual/delete/<business_id>', views.InvestorIndivDelete, name='individual-delete'),
    path('company/delete/<business_id>', views.InvestorCompanyDelete, name='company-delete'),
    path('company', views.investor_company, name='company'),
    path('individual_update/<business_id>', views.IndividualUpdate, name='individual-update'),
    path('company_update/<business_id>', views.CompanyUpdate, name='company-update'),
    url('ajax/validate/$', views.validate, name='investor-validate'),
    url('ajax/validate/indiv/', views.validate_indiv, name='business-validate-indiv'),
    url('ajax/validate/company/', views.validate_company, name='business-validate-company'),

]