from channels.consumer import SyncConsumer
from channels.generic.websocket import WebsocketConsumer
import json
from random import randint
from time import sleep

class WSConsumer(SyncConsumer):
    def websocket_connect(self, event):
        self.send({
            'type':'websocket.accept',
        })
        for i in range(1000):
            message = {
                "message":randint(0,100)
            }
            self.send({
                "type":"websocket.send",
                "text":json.dumps(message),
            })
            sleep(1)

    def websocket_disconnect(self, event):
        self.send({
            'type':'websocket.discard'
        })

    def websocket_receive(self, event):
        self.send({
            "type":"websocket.send",
            "text":event["text"],
        })

