from rest_framework import serializers
from .models import *

class PostSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')  # User should be read-only
    like_count = serializers.IntegerField(read_only=True)  # Prevent users from setting like count
    comment_count = serializers.IntegerField(read_only=True)  # Prevent users from setting comment count

    class Meta:
        model = Post
        fields = ['id', 'title', 'description', 'image', 'created_at', 'user', 'like_count', 'comment_count']

class LikeSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    class Meta:
        model = Like
        fields = "__all__"

class CommentSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')    
    class Meta:
        model = Comment
        fields = "__all__"
        


