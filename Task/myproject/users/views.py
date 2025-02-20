from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from .models import *
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
    def post(self , request ):
        serializer = UserSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

