# django settings
from django.shortcuts import get_object_or_404
# drf
from rest_framework import status
from rest_framework import viewsets
from rest_framework.response import Response
# redefined user
from api.serializers import UserSerializer
from api.models import User

User = User

class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class AuthViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    # def create(self, request):
    #     return Response(status=status.HTTP_201_CREATED)

    def post(self, request):
        return Response(status=status.HTTP_200_OK)
