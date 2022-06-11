from rest_framework import serializers
from .models import User
from rest_framework.serializers import ModelSerializer
from django.contrib.auth import authenticate

class RegisterSerializer(ModelSerializer):
    password = serializers.CharField(max_length=128, min_length=8, write_only=True)

    class Meta:
        model = User
        fields = ("email", "full_name", "password")

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)
    
class LoginSerializer(ModelSerializer):
    email = serializers.EmailField(write_only=True)
    password = serializers.CharField(max_length=128, write_only=True)

    def validate(self, data):
        email = data.get('email', None)
        password = data.get('password', None)
        user = authenticate(username=email, password=password)
        return user

class PasswordSerializers(serializers.Serializer):
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'full_name' ,'password')