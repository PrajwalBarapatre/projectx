from django.urls import path,  include
from profiles import views
import seller1.views as sell_views
import seller1.sms as sms
# from rest_framework.urlpatterns import format_suffix_patterns

handler404 = views.handler404
handler500 = views.handler500

urlpatterns = [
    path('', views.home_view, name='index'),
    path('subscribe', views.subscription, name='subscription'),
    path('pricing', views.pricing, name='pricing'),
    path('terms', views.terms, name='terms'),
    path('process_subscription', views.process_subscription, name='process_subscription'),
    path('payment-done/', views.payment_done, name='payment_done'),
    path('payment-cancelled/', views.payment_canceled, name='payment_canceled'),
    path('signup', views.register_view, name='signup'),
    path('user_profile', sell_views.user_profile, name='user-profile'),
    path('user_dashboard', sell_views.indiv_dash, name='user-dash'),
    path('user_dashboard2', sell_views.indiv_dash2, name='user-dash2'),
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
    path('retive_notif', views.notif_data, name='retive_notif'),
    path('delete_profile', views.delete_profile, name='delete_profile'),
    path('clear_notif', views.clear_notif, name='clear_notif'),
    path('feedback_submit', views.feedback_submit, name='feedback_submit'),
    path('auth_error', views.auth_error, name='auth_error'),
    path('unlock_premium', sell_views.unlock_premium, name='unlock_premium'),

]
