from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from .models import Converstation, Message
from .serializer import MessageSerializer, ConversationSerializer

class CreateConversationAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        participants_usernames = request.data.get('participants', [])
        participants = User.objects.filter(username__in=participants_usernames)
        
        if not participants.exists():
            return Response({"detail": "Participants not found."}, status=status.HTTP_404_NOT_FOUND)

        conversation = Converstation.objects.create()
        conversation.participants.set(participants)
        conversation.save()

        serializer = ConversationSerializer(conversation)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class SendMessageAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, conversation_id):
        conversation = get_object_or_404(Converstation, id=conversation_id)

        if request.user not in conversation.participants.all():
            return Response({"detail": "You are not a participant in this conversation."}, status=status.HTTP_400_BAD_REQUEST)

        content = request.data.get('content', '')
        if not content:
            return Response({"detail": "Message content cannot be empty."}, status=status.HTTP_400_BAD_REQUEST)

        message = Message.objects.create(
            conversation=conversation,
            sender=request.user,
            receiver=conversation.participants.exclude(id=request.user.id).first(),
            content=content
        )

        message_serializer = MessageSerializer(message)
        return Response(message_serializer.data, status=status.HTTP_201_CREATED)


class GetConversationMessagesAPIView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, conversation_id):
        conversation = get_object_or_404(Converstation, id=conversation_id)

        if request.user not in conversation.participants.all():
            return Response({"detail": "You are not a participant in this conversation."}, status=status.HTTP_400_BAD_REQUEST)

        messages = conversation.messages.all().order_by('-created_at')
        serializer = MessageSerializer(messages, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class GetConversationsAPIView(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        conversations = Converstation.objects.filter(participants=request.user)
        serializer = ConversationSerializer(conversations, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
