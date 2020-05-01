from django.conf.urls import url
from django.urls import path

from . import views

urlpatterns = [
    # path('api/', views.ChatListView.as_view()),
    path('upload_files', views.upload_file, name='upload-file'),
    path('close', views.chat_close, name='chat-close'),
    path('pdf_view/<file_name>', views.pdf_view, name='pdf-view'),
    path('make-invest', views.make_chat_invest, name='chat-invest'),
    path('make-advise', views.make_chat_advisor, name='chat-advise'),
    path('make-sell', views.make_chat_seller, name='chat-sell'),
    path('fetch-sell/<business_id>', views.fetch_sell_id, name='fetch-sell-id'),
    path('api/<username>', views.get_all_chats),
    path('create/', views.ChatCreateView.as_view()),
    path('<pk>', views.ChatDetailView.as_view()),
    path('<pk>/update/', views.ChatUpdateView.as_view()),
    path('<pk>/delete/', views.ChatDeleteView.as_view()),
    url(r'^$', views.index, name='index'),
    path('<room_name>/', views.room, name='room'),
    path('check_chat', views.staff_check_connection, name='check_chat'),
    path('close_service', views.staff_close_connection, name='close_service'),
    path('send_whatsapp_message', views.send_whatsapp_message, name='send_whatsapp_message'),
    path('handle_incoming_messages', views.handle_incoming_messages, name='handle_incoming_messages'),


]