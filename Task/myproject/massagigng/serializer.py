from rest_framework import serializers
from .models import Converstation, Message
from users.models import User

class MessageSerializer(serializers.ModelSerializer):
    sender = serializers.ReadOnlyField(source='sender.username')
    receiver = serializers.ReadOnlyField(source='receiver.username')

    class Meta:
        model = Message
        fields = ['id', 'sender', 'receiver', 'content', 'created_at', 'read_at']

class ConversationSerializer(serializers.ModelSerializer):
    participants = serializers.SlugRelatedField(slug_field='username', queryset=User.objects.all(), many=True)

    class Meta:
        model = Converstation
        fields = ['id', 'participants', 'created_at']