from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import GenericAPIView
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from .serializers import UserSerializer, PasswordSerializers, RegisterSerializer
from .models import User
from .permissions import UsersPermission


class UserViewSet(ModelViewSet):
    permission_classes = [UsersPermission]
    serializer_class = RegisterSerializer
    queryset = User.objects.all()

    @action(detail=True, methods=['POST'])
    def set_password(self, request, pk=None):
        user = self.get_object()
        serializer = PasswordSerializers(data=request.data)
        if serializer.is_valid:
            user.set_password(serializer.validated_data['new_password'])
            user.save()
            return Response({'status': 'password set'})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class RegisterAPIView(GenericAPIView):
    serializer_class = RegisterSerializer
    # permission_classes = []

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return user
    
    def get_permissions(self):
        if self == 'create':
            return [AllowAny()]
        else:
            return super().get_permissions()