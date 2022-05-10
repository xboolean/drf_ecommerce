from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .serializers import UserSerializer
from .models import User
from .permissions import UsersPermission


class UserViewSet(ModelViewSet):
    permissions_class = [UsersPermission]
    serializer_class = UserSerializer
    queryset = User.objects.all()