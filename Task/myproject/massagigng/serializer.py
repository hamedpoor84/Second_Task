from rest_framework import serializers
from .models import Converstation, Message
from users.models import User

class MessageSerializer(serializers.ModelSerializer):
    sender = serializers.ReadOnlyField(source='sender.username')
    receiver = serializers.ReadOnlyField(source='receiver.username')
    created_at = serializers.ReadOnlyField()

    class Meta:
        model = Message
        fields = "__all__"

class ConversationSerializer(serializers.ModelSerializer):
    participants = serializers.SlugRelatedField(slug_field='username', queryset=User.objects.all(), many=True)
    created_at = serializers.ReadOnlyField()
    class Meta:
        model = Converstation
        fields = ['id', 'participants', 'created_at']