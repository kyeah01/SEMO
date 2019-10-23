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
            - 버전관리를 위해 갱신되어야 할 내용을 뒤에 더해주는 식으로 갱신
        
        3) delete
            - variable path 이용
            - detail 정보 delete

    """
    def get(self, request, obj_pk):
        apiSite = get_object_or_404(APISite, pk=obj_pk)
        serializer = APISiteDetailSerializer(apiSite)
        return Response(serializer.data)

    def post(self, request, obj_pk):
        apiSite = get_object_or_404(APISite, pk=obj_pk)
        serializer = APISiteDetailSerializer(instance=apiSite, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, obj_pk):
        apiSite = get_object_or_404(APISite, pk=obj_pk)
        apiSite.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

