from rest_framework import serializers
from .models import User
from rest_framework.serializers import ValidationError
from django.contrib.auth import authenticate
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
import jwt
from django.conf import settings

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
    
    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

class TokenSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        payload = jwt.decode(data['access'], settings.SECRET_KEY, algorithms='HS256')
        user = User.objects.get(id=payload['user_id'])
        if not user.is_active:
            raise ValidationError("Your account has not been activated yet.")
        return data
        
        
        
        
