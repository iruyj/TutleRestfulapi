import datetime
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework.views import APIView

from .models import Cure
from .serializers import CureSerializer
# Create your views here.

# create, list
class Cures(APIView):
    def post(self,request):
        user_email = request.data.get('user_email','')
        stretch_num = request.data.get('stretch',0)
        status = request.data.get('status',0)

        cure = Cure.objects.create(user_email=user_email, stretch=stretch_num, status=status )
        
        return Response(dict(msg="cure 생성 완료",date=cure.created, status= cure.status, stretch_num= cure.stretch))
    def get(self, request):
        all = Cure.objects.all()
        serializers = CureSerializer(all, many=True)
        return Response(serializers.data)

class CureUser(APIView):
    def get(self, request):
        user_email = request.query_params.get('user_email', "")

        cures = Cure.objects.filter(user_email=user_email)
        serializers = CureSerializer(cures, many=True)
        return Response(serializers.data)


# Select today's stretchLogs
class DaysSelect(APIView):
    def get(self, request):
        day = request.query_params.get('date',datetime.date)
        user_email = request.query_params.get('user_email', "")

        cures = Cure.objects.filter(created=day,user_email=user_email)
        serializers = CureSerializer(cures, many=True)
        return Response(serializers.data)

class DaysDistinct(APIView):
    def get(self, request):
        user_email = request.query_params.get('user_email', "")

        cures = Cure.objects.filter(user_email=user_email)
        days = cures.value_list('created',flat=True).distinct().order_by('created')
        return JsonResponse(days, status=200)

@api_view(['GET','PUT','DELETE'])
def cure_select(request,id):
    cure = Cure.objects.filter(id=id).first()
    if request.method == 'GET':
        return Response(CureSerializer(cure).data)

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
