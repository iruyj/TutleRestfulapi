import datetime
from django.http import HttpResponse, JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status, generics, mixins
from rest_framework.parsers import JSONParser
from rest_framework.views import APIView

from .models import Cure
from .serializers import CureSerializer
# Create your views here.

# create, list
class Cures(APIView):
    def post(self,request):
        user_email = request.data.get('user_email','')
        end_time = request.data.get('end_time',None)
        stretch_num = request.data.get('stnum',0)
        status = request.data.get('status',0)

        cure = Cure.objects.create(user_email=user_email, end=end_time, stretch=stretch_num, status=status )
        
        return Response(dict(msg="cure 생성 완료",end_time=cure.end, start_time=cure.start,
                             date=cure.created, status= cure.status, stretch_num= cure.stretch))
    def get(self, request):
        all = Cure.objects.all()
        serializers = CureSerializer(all, many=True)
        return Response(serializers.data)

class CureUser(APIView):
    def get(self, request):
        user_email = ''
        if request.query_params:
            user_email = request.query_params.get('user_email', "")

        cures = Cure.objects.filter(user_email=user_email)
        cure_list = []
        for cure in cures:
            cure_list.append(dict(user_email=cure.email, start_time=cure.start, end_time=cure.end, state=cure.state,stretch=cure.stretch, created=cure.created))

        return Response(dict(cures=cure_list))


# Select today's stretchLogs
class TodaySelect(APIView):
    def get(self, request):
        today = datetime.date
        user_email = ''
        if request.query_params:
            user_email = request.query_params.get('user_email', "")

        cures = Cure.objects.filter(created=today,user_email=user_email)
        cure_list = []
        for cure in cures:
            cure_list.append(dict(user_email=cure.email, start_time=cure.start, end_time=cure.end, state=cure.state,stretch=cure.stretch, created=cure.created))

        serializers = CureSerializer(cure_list, many=True)
        return Response(serializers.data)


def cure_select(request,id):
    cure = Cure.objects.filter(id=id)
    if request.method == 'GET':
        data = (dict(user_email=cure.email, start_time=cure.start, end_time=cure.end, state=cure.state,
                                  stretch=cure.stretch, created=cure.created))

        return Response(dict(cures=data))

    if request.method == 'PUT':
        data = JSONParser().parse(request)
        serial = CureSerializer(cure, data=data)

        if serial.is_valid():
            serial.save()
            return JsonResponse(serial.data,status=201)
        return JsonResponse(serial.errors, status=400)

    if request.method == 'DELETE':
        cure.delete()
        return HttpResponse(status=204)
