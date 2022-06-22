import jwt
from django.conf import settings
from django.db import transaction
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import GenericAPIView
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from .serializers import AccountConfirmationSerializer, UserSerializer, TokenSerializer
from .models import User
from .permissions import UsersPermission
from .utils import Util

class UserViewSet(ModelViewSet):
    permission_classes = [UsersPermission]
    serializer_class = UserSerializer
    queryset = User.objects.all()

    @transaction.atomic
    def perform_create(self, serializer):
        account = serializer.save()
        user = User.objects.get(email=account.email)
        token = RefreshToken.for_user(user).access_token
        body = f"Ваш аккаунт на drf-ecommerce успешно создан!\
        Для активации учетной записи укажите этот токен в документации по пути: 'auth/account-confirm/': {token}"
        data = {'mail_subject': settings.EMAIL_MESSAGES['registration']['subject'], 'to_email': account.email, 'mail_body': body}
        Util.send_email(data)
        return Response(data=serializer.data, status=status.HTTP_201_CREATED)
    
    @swagger_auto_schema(auto_schema=None)
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)
    
    @swagger_auto_schema(auto_schema=None)
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)
    
    @swagger_auto_schema(auto_schema=None)
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)

class VerifyEmail(GenericAPIView):
    serializer_class = AccountConfirmationSerializer
    token_param_config = openapi.Parameter('token', in_=openapi.IN_QUERY, description='Description', type=openapi.TYPE_STRING)

    @swagger_auto_schema(manual_parameters=[token_param_config])
    def get(self, request):
        token=request.GET.get('token')
        try:
            payload = jwt.decode(token, settings.SECRET_KEY, algorithms='HS256')
            user = User.objects.get(id=payload['user_id'])
            if not user.is_active:
                user.is_active = True
                user.save()
                return Response({'email': 'Yout account succesfully activated!'}, status=status.HTTP_200_OK)
        except jwt.ExpiredSignatureError as e:
            return Response({'error': 'Token has been expired!'}, status=status.HTTP_400_BAD_REQUEST)
        except jwt.DecodeError as e:
            return Response({'error': 'Invalid token has been passed!'}, status=status.HTTP_400_BAD_REQUEST)

class TokenCreateView(TokenObtainPairView):
    serializer_class = TokenSerializer