from django.shortcuts import render
from django.shortcuts import get_object_or_404

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from api.models import APISite, EditedList
from api.serializers import APISiteListSerializer, APISiteDetailSerializer, EditRequestListSerializer


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
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        self.permission_denied(request)
        serializer = APISiteDetailSerializer(request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class APIDetailView(APIView):
    """
        19.10.23 AM 9:50
        하나의 api view를 확인하고 관리할 수 있게 하는 view

        1) get
            - variable path 이용
            - 하나의 api 사이트의 detail 정보 response
        
        2) patch
            - variable path 이용
            - detail 정보 수정
        
        3) delete
            - variable path 이용
            - detail 정보 delete

    """
    def get(self, request, site_pk):
        apiSite = get_object_or_404(APISite, pk=site_pk)
        serializer = APISiteDetailSerializer(apiSite)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def patch(self, request, site_pk):
        self.permission_denied(request)
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

    
class DocsRequestView(APIView):
    """
        19.10.25 PM 3:00
        user가 수정 / 삭제 / 등록을 요청하는 view
        
        1) get
            - admin이 user들이 요청한 edit requests를 전부 확인함.
            - admin인지 확인하는 과정 필요.

        2) post
            - user가 api site의 등록/수정/삭제 등 변경 요청

    """

    def get(self, requset):
        editLists = EditedList.objects.all()
        serializer = EditRequestListSerializer(editLists)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = EditRequestListSerializer(request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)