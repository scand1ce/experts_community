import json
from channels.generic.websocket import AsyncWebsocketConsumer
from django.contrib.auth.decorators import login_required

from users.models import CustomUser


class ChatConsumer(AsyncWebsocketConsumer):

    async def connect(self):
        self.user = self.scope['user']
        self.room_name = 'general'
        self.room_group_name = 'general'

        if not self.user.is_authenticated:
            await self.close()

            # Join room group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name

        )

        await self.accept()

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    # Receive message from WebSocket
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        # Send message to room group
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message
            }
        )

    # Receive message from room group
    async def chat_message(self, event):
        message = event['message']

        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'message': message
        }))

