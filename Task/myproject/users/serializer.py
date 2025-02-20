from rest_framework import serializers
from .models import *

class UserSerializer(serializers.ModelSerializer) :
    password = serializers.CharField(write_only=True)  # Allow password input but not output
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'email', 'password']  # Include only necessary fields


