from django.shortcuts import render
from django.shortcuts import get_list_or_404, get_object_or_404

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from api.models import Ratings
from api.serializers import RatingSerializer

from datetime import datetime

class RatingView(APIView):
    """
        19.10.23 AM 10:23
        rating을 조회하는 뷰

        1) get
            - rating 목록을 조회
            - site_pk를 받으면 해당 site의 rating으로 목록 제한
            - user_pk를 받으면 해당 user의 rating으로 목록 제한
        
        2) post
            - auth인증 된 유저가 rating 등록
        * 현재 로그인된 user정보를 저장하도록 수정해야 함.

    """

    def get(self, request):
        ratings = Ratings.objects.all()
        site_pk = request.GET.get('site_pk')
        user_pk = request.GET.get('user_pk')
        if site_pk is not None:
            ratings = ratings.filter(apiSite__pk=site_pk)
        if user_pk is not None:
            ratings = ratings.filter(user__pk=user_pk)
        serializer = RatingSerializer(ratings, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = RatingSerializer(request.data)
        if serializer.is_valid():
            serializer.save(rating_date = round(datetime.now().timestamp()))
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class RatingEditView(APIView):
    """
        19.10.23 AM 10:36
        rating을 수정/삭제하는 뷰

        1) patch
            - auth인증 된 유저가 본인의 rating일때 rating 수정

        2) delete
            - auth인증 된 유저가 본인의 rating일때 rating 삭제

        * 본인일때만 수정/삭제하도록 추후 업데이트 필요.
    """

    def patch(self, request, rating_pk):
        ratings = get_object_or_404(Ratings, pk=rating_pk)
        serializer = RatingSerializer(instance=ratings, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save(rating_date = round(datetime.now().timestamp()))
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, rating_pk):
        ratings = get_object_or_404(Ratings, pk=rating_pk)
        ratings.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)