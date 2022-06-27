import jwt
from rest_framework import serializers
from .models import User, CustomerProfile
from rest_framework.serializers import ValidationError
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.conf import settings

class AccountConfirmationSerializer(serializers.Serializer):
    token = serializers.CharField(max_length=229)
    class Meta:
        model = User
        fields = ['token']

class UserSerializer(serializers.ModelSerializer):
    address = serializers.CharField(source='profile.address')
    class Meta:
        model = User
        fields = ('email', 'full_name' ,'password', 'address')
        extra_kwargs = {'password': {'write_only': True}}
    
    def create(self, validated_data):
        print(validated_data)
        profile = validated_data.pop('profile')
        user = User.objects.create_user(**validated_data)
        if getattr(user, 'is_staff') == False:
            CustomerProfile.objects.create(user=user, address=profile['address'])
        return user

class TokenSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        payload = jwt.decode(data['access'], settings.SECRET_KEY, algorithms='HS256')
        user = User.objects.get(pkid=payload['user_id'])
        if not user.is_active:
            raise ValidationError("Your account has not been activated yet.")
        return data
        
        
        
