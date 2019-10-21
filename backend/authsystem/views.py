from django.shortcuts import render
from django.contrib.auth import authenticate, login as authLogin

from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

# token 인증을 위한 라이브러리
from .serializers import *

class SignUpView(APIView):
    def post(self, request):
        pass

class LoginView(APIView):
    def post(self, request):
        serializer = LoginUserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.authenticate
        return Response({
                    "user": user,
                })