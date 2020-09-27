from chat.models import Chat
from django.views.generic import (CreateView)


class ChatView(CreateView):
    model = Chat
    pass
