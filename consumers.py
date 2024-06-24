import json
from channels.generic.websocket import AsyncWebsocketConsumer

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()
        print("Connect")
        await self.send(text_data=json.dumps({
            'message': "hello Amon"
        }))
    async def disconnect(self, close_code):
        pass
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        print(text_data)
        message = text_data_json['message']
        #await self.send(text_data=json.dumps({
        await self.send(text_data=json.dumps({
            'message': message
        }))
        print(message)