from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.contrib import admin

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser, SAFE_METHODS

from api.models import APISite
from api.serializers import APISiteListSerializer, APISiteDetailSerializer


class APIListView(APIView):
    """    
        전체 api사이트를 조회하고 / 새로운 api 사이트를 등록할 수 있게 하는 view

        1) get 
            - 모든 유저가 모두 접근가능
            - 전체 list를 조회할 수 있게 함
        2) post 
            - admin만 가능
            - 새로운 api site를 등록할 수 있게 함.
    """
    def has_permission(self, request):
        if request.method in SAFE_METHODS:
            return True
        return request.user == admin

    def get(self, request):
        apiSiteList = APISite.objects.all()
        serializer = APISiteListSerializer(apiSiteList, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        if not self.has_permission(request):
            return Response(
                data = {"detail": "자격 인증데이터(authentication credentials)가 제공되지 않았습니다."}, 
                status=status.HTTP_401_UNAUTHORIZED)
        serializer = APISiteDetailSerializer(request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class APIDetailView(APIView):
    """
        19.10.23 AM 9:50
        하나의 api view를 확인하고 관리할 수 있게 하는 view
        admin만 접근가능.

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

    permission_classes = (IsAdminUser,)

    def get(self, request, site_pk):
        apiSite = get_object_or_404(APISite, pk=site_pk)
        serializer = APISiteDetailSerializer(apiSite)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def patch(self, request, site_pk):
        apiSite = get_object_or_404(APISite, pk=site_pk)
        serializer = APISiteDetailSerializer(instance=apiSite, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, site_pk):
        apiSite = get_object_or_404(APISite, pk=site_pk)
        apiSite.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)