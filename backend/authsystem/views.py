from django.shortcuts import render
from django.contrib.auth import authenticate, login as authLogin

from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

class LoginView(APIView): 
    def post(self, request):
        # serializer, form 사용시 변경해야함
        username = request.data['username']
        password = request.data['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            authLogin(request, user)
            return Response(status=status.HTTP_200_OK)
        return Response(status=status.HTTP_403_FORBIDDEN)