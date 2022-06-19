from django.forms import CharField
from rest_framework import serializers
from .models import User
from rest_framework.serializers import ValidationError
from django.contrib.auth import authenticate
from .tokens import TokenValidator

class LoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(write_only=True)
    password = serializers.CharField(max_length=128, write_only=True)

    def validate(self, data):
        email = data.get('email', None)
        password = data.get('password', None)
        user = authenticate(username=email, password=password)
        return user

class AccountConfirmationSerializer(serializers.Serializer):
    token = serializers.CharField(max_length=229)

    class Meta:
        model = User
        fields = ['token']
        
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'full_name' ,'password')
        read_only_fields = ('id',)
