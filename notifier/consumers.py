import json
from pprint import pprint

from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
from rest_framework.renderers import JSONRenderer

from human_resources.inspector.model import InspectorModel
from human_resources.inspector.permission import IsInspector
from problem_solving.problem.model import ProblemModel
from problem_solving.problem.serializer import ProblemSerializer


class InspectorConsumer(WebsocketConsumer):
    def connect(self):
        self.room_name = self.room_group_name = phone_number = self.scope['url_route']['kwargs']['phone']
        password = self.scope['url_route']['kwargs']['password']
        if IsInspector.is_inspector(phone_number, password):
            async_to_sync(self.channel_layer.group_add)(
                phone_number,
                self.channel_name
            )

            self.accept()

    def disconnect(self, code):
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )

    def receive(self, text_data=None, bytes_data=None):
        # text_data_json = json.loads(text_data)
        # message = text_data_json['message']

        inspector = InspectorModel.objects.get(phone_number=self.room_group_name)
        problems = ProblemModel.objects.filter(assigned_to_inspector_id=inspector.id)
        pprint(problems)
        problem_serializer = ProblemSerializer(problems, many=True)
        content = JSONRenderer().render(problem_serializer.data)
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type': 'fetch_problems',
                'message': str(content)
            }
        )

    # Receive message from room group
    def fetch_problems(self, event):
        message = event['message']

        self.send(text_data=json.dumps({
            'message': message
        }))


class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name

        # Join room group
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )

        self.accept()

    def disconnect(self, close_code):
        # Leave room group
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )

    # Receive message from WebSocket
    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        # Send message to room group
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message
            }
        )

    # Receive message from room group
    def chat_message(self, event):
        message = event['message']

        # Send message to WebSocket
        # self.send(text_data=json.dumps({
        #     'message': message
        # }))
        self.send(text_data=json.dumps({
            'message': {
                'id': 323,
                'description': 'some description.',
                'city': 'tehran'
            }
        }))
