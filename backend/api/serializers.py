from rest_framework import serializers
from .models import APISite, EditedList, RegisterList, Ratings

class APISiteListSerializer(serializers.Serializer):
    class Meta:
        model = APISite
        fields = '__all__'

class APISiteDetailSerializer(serializers.Serializer):
    class Meta:
        model = APISite
        fields = '__all__'

class EditRequestListSerializer(serializers.Serializer):
    class Meta:
        model = EditedList
        fields = ('pk', 'target', 'title')
    
class EditRequestDetailSerializer(serializers.Serializer):
    class Meta:
        model = EditedList
        fields = '__all__'