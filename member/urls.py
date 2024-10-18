from django.urls import path
from .views import send_messages
urlpatterns = [
    path('messages', send_messages,  name='messages'),

]


