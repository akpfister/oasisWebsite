# chat/routing.py
from django.conf.urls import url
from django.urls import path, re_path

from . import consumers

websocket_urlpatterns = [
    path('ws/help/<room_name>/', consumers.ChatConsumer),
]
