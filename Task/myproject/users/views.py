from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated , AllowAny
from django.shortcuts import get_object_or_404
from .models import *
from django.contrib.auth.hashers import make_password
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from .serializer import *


class GetUSerByIDAPIView(APIView):
    permission_classes = [IsAuthenticated]
    def get_object(self, pk):
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            return None
        
    @swagger_auto_schema(
        operation_description="get profile of a user",
        responses={200: UserSerializer(many=True)}
    )
    def get(self, request, User_ID=None):
        user = User.objects.get(pk=User_ID) 
        if User_ID is None :
            user = request.user
            serializer = UserSerializer(user)
            return Response(serializer.data)
        else:
            serializer = UserSerializer(user)
            if user is None:
                return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)
            return Response(serializer.data)

class CreateUSerAPIView(APIView):
    permission_classes = [AllowAny] 
    @swagger_auto_schema(
        operation_description="Create a new post",
        request_body=UserSerializer,
        responses={201: UserSerializer()}
    )
    def post(self, request):
        data = request.data
        password = data.get('password')
        if password:
            data['password'] = make_password(password)  # Hash the password before saving

        serializer = UserSerializer(data=data)
        if serializer.is_valid():
            user = serializer.save()  # Save the user
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

