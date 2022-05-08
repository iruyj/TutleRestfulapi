import datetime

from django.db.models.functions import Log
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.parsers import JSONParser
from .models import Cure
from .serializers import CureSerializer
# Create your views here.

@api_view(['GET','POST'])
def cures_list(request):
    if request.method == 'GET':
        query_set = Cure.objects.all()
        serializer = CureSerializer(query_set, many=True)
        return Response(serializer.data)
    else:
        data = JSONParser().parse(request)
        serializer = CureSerializer(data=data)
        if serializer.is_valid():   # serializer에 올라온 데이터를 검사했을때 괜찮으면
            serializer.save()   # 정상적으로 객체 생성
            return Response(serializer.data, status=status.HTTP_201_CREATED)    # 성공
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)      # 실패

@api_view(['GET'])
def today_list(request):    # 오늘 날짜 디비 리스트만 가져오기
    today = datetime.date.today()
    start_date = datetime.datetime.strptime(str(today.year) + " " + str(today.month) + " " + str(today.day), '%Y %m %d')
    end_date = datetime.datetime.strptime(str(today.year) + " " + str(today.month) + " " + str(today.day) + " 23:59", '%Y %m %d %H:%M')
    try:
        log = Cure.objects.get(created_at__range=[start_date, end_date])
    except Cure.DoesNotExist:
        log = None

@api_view(['GET'])
def user_list(request, user):   # user의 모든 스트레칭 기록 가져오기
    pass
