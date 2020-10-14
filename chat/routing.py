from django.conf.urls import url
from django.urls import re_path
from . import consumers
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter

websocket_urlpatterns = [
    url(r'ws/chat/general/$', consumers.ChatConsumer),
]

application = ProtocolTypeRouter({
    # (http->django views is added by default)
    'websocket': AuthMiddlewareStack(
        URLRouter(
            websocket_urlpatterns
        )
    ),
})
