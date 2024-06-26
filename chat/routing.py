from django.conf.urls import url
from django.urls import path
from . import consumers

websocket_urlpatterns = [
    # url(r'^ws/chat/(?P<room_name>[^/]+)/$', consumers.ChatConsumer),
    path('ws/chat/<room_name>/', consumers.ChatConsumer),
    path('ws/staff-chat/<room_name>/', consumers.StaffChatConsumer),
]