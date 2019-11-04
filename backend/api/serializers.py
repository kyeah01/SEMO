import json

from django.forms.models import model_to_dict
from rest_framework import serializers

from .models import APISite, EditedList, RegisterList, Ratings, GuideCode, EndPoints

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

class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ratings
        fields = '__all__'

class EndPointsSerializer(serializers.ModelSerializer):
    code = serializers.SerializerMethodField('get_guide_code')

    class Meta:
        model = EndPoints
        fields = '__all__'
        extra_fields = ('code',)

    def get_guide_code(self, obj):
        queryString = json.loads(model_to_dict(obj).get('queryString'))
        replacement_List = {
            key : value.get('sample') for key, value in queryString.items() if value.get('required')
        }

        guides = [guide.__dict__ for guide in GuideCode.objects.all()]
        for guide in guides:
            guide.pop('_state', None)

        url = obj.apisite.url + json.loads(obj.pathParams).get('sample')

        for guide in guides:
            guide['code'] = guide['code'].replace('{{ method }}', obj.method.lower())
            guide['code'] = guide['code'].replace('{{ url }}', url)
            if obj.method == "POST":
                guide['code'] = guide['code'].replace('{{ params }}', str(replacement_List))
                guide['code'] = guide['code'].replace('params', 'data')
            else:
                guide['code'] = guide['code'].replace('{{ params }}', str(replacement_List))
        return guides