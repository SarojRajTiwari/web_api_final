from django.shortcuts import render
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny
from apis.accounts.serializers import UserSerializer

class CreateUserAPIView(CreateAPIView):
    permission_classes = [AllowAny]
    serializer_class = UserSerializer