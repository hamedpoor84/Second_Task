from django.urls import path
from .views import CreateConversationAPIView, SendMessageAPIView, GetConversationMessagesAPIView, GetConversationsAPIView

urlpatterns = [
    path('conversations/', GetConversationsAPIView.as_view(), name='get-conversations'),
    path('conversations/create/', CreateConversationAPIView.as_view(), name='create-conversation'),
    path('conversations/<int:conversation_id>/messages/', GetConversationMessagesAPIView.as_view(), name='get-messages'),
    path('conversations/<int:conversation_id>/messages/send/', SendMessageAPIView.as_view(), name='send-message'),
]
