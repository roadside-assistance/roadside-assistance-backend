from django.urls import re_path

from . import consumers

websocket_urlpatterns = [
    re_path(r'ws/notifier/(?P<room_name>\w+)/$', consumers.ChatConsumer.as_asgi()),
    re_path(r'ws/notifier/inspector/(?P<phone>\w+)/(?P<password>\w+)/$', consumers.InspectorConsumer.as_asgi()),
]
