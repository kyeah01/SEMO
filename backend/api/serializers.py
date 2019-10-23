from rest_framework import serializers
from .models import APISite, EditedList, RegisterList, Ratings

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