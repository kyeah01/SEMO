from rest_framework import serializers
from django.contrib.auth import authenticate
from django.contrib.auth import get_user_model
from .models import APISite, EditedList, RegisterList, Ratings

User = get_user_model()

class APISiteListSerializer(serializers.ModelSerializer):
    class Meta:
        model = APISite
        fields = ('title', 'url', 'category')

class APISiteDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = APISite
        fields = '__all__'

class EditRequestListSerializer(serializers.ModelSerializer):
    class Meta:
        model = EditedList
        fields = ('pk', 'target', 'title')

class EditRequestDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = EditedList
        fields = '__all__'

# 회원가입 시리얼라이저
class CreateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "username", "password")
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        user = User.objects.create_user(
            validated_data["username"], None, validated_data["password"]
        )
        return user

# 로그인 시리얼라이저
class LoginUserSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Unable to log in with provided credentials.")

# 접속 유지중인지 확인할 시리얼라이저
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "username")
