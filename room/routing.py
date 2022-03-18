import imp
# from django.urls import path
from django.urls import re_path
from . import consumers


websocket_urlpatterns = [
    re_path(r'ws/rooms/(?P<room_name>\w+)/$', consumers.ChatConsumer.as_asgi())
    # path('rooms/<str:room_name>/', consumers.ChatConsumer.as_asgi()),
]

