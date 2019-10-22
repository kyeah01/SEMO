from django.shortcuts import render
from django.shortcuts import get_list_or_404, get_object_or_404

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from api.models import APISite
from api.serializers import APISiteListSerializer, APISiteDetailSerializer


class APIListView(APIView):
    """    
        전체 api사이트를 조회하고 / 새로운 api 사이트를 등록할 수 있게 하는 view

        1) get 
            - 전체 list를 조회할 수 있게 함
        2) post 
            - 새로운 api site를 등록할 수 있게 함.
    """
    def get(self, request):
        apiSiteList = APISite.objects.all()
        serializer = APISiteListSerializer(apiSiteList, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = APISiteDetailSerializer(request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class APIDetailView(APIView):
    """
        하나의 api view를 확인하고 관리할 수 있게 하는 view

        1) get
            - variable path 이용
            - 하나의 api 사이트의 detail 정보 response
        2) patch
            - variable path 이용
            - detail 정보를 갱신하기 위한 새로운 값 더해줌
        
        3) delete
            - variable path 이용
            - detail 정보 delete

    """
    def get(self, request):
        pass

    def post(self, request):
        pass