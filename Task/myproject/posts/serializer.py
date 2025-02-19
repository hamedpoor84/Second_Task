from rest_framework import serializers
from .models import *

class PostSerializer(serializers.ModelSerializer) :
    user = serializers.ReadOnlyField(source='user.username')
    class Meta:
        model = Post
        fields = '__all__'
        read_only_fields = ['id' , 'titile' , 'created_at' , 'user', 'comment_count', 'like_count']

class LikeSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    class Meta:
        model = Like
        fields = "__all__"
        read_only_fields = ['id' , 'post' , 'created_at' , 'user']


class CommentSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')    
    class Meta:
        model = Comment
        fields = "__all__"
        read_only_fields = ['id' , 'content' , 'post' , 'created_at' , 'user']
        


