from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from .models import *
from .serializer import *

class GetFollowbyIDAPIView(APIView):
    permission_classes = [IsAuthenticated]
    def get_object(self, pk):
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            return None

    def post (self, request, User_ID):
        user = User.objects.get(pk=User_ID)
        follow , created = Follow.objects.get_or_create(follower=request.user, following=user)
        if created:
            return Response({"message": "Followed"}, status=status.HTTP_201_CREATED)
        else:    
            follow.delete()
            return Response({"message": "Unfollowed"}, status=status.HTTP_204_NO_CONTENT)


class GetFollowersAPIView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, User_ID=None):
        user = User.objects.get(pk=User_ID)
        if User_ID is not None:
            followers = user.followers.all()
            serializer = FollowSerializer(followers, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            followers = request.user.followers.all()
            serializer = FollowSerializer(followers, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

class GetFollowingAPIView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, User_ID=None):
        user = User.objects.get(pk=User_ID) 
        if User_ID is not None:
            following = user.following.all()
            serializer = FollowSerializer(following, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            following = request.user.following.all()
            serializer = FollowSerializer(following, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)