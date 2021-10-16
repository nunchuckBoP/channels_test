from django.urls import path
from .consumers import WSConsumer

channel_routing = [
    path('ws/some_url/', WSConsumer.as_asgi())
]