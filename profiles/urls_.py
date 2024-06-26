from django.urls import path,  include
from . import views
import seller1.views as sell_views
import seller1.sms as sms
# from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('', views.home_view, name='index'),
    path('signup', views.register_view, name='signup'),
    path('user_profile', sell_views.user_profile, name='user-profile'),
    path('user_dashboard', sell_views.indiv_dash, name='user-dash'),
    path('check_email', views.check_email, name='check-email'),
    path('check_username', views.check_username, name='check-username'),
    path('clear_notif', views.clear_notif, name='clear-notif'),
    path('user/check_email', sms.check_email_otp, name='user-email-otp'),
    path('edit_profile', views.edit_profile , name='edit-profile'),
    path('login', views.login_view, name='login'),
    path('logout', views.logout_view, name='logout'),
    path('get_user', views.getUser.as_view(), name='get-user'),
    path('con_password', views.password_confirm, name='con-password'),
    path('chng_password', views.password_change, name='chng-password'),

]