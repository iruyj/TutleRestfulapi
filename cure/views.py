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

# class CureCreate(generics.GenericAPIView,
#                  mixins.CreateModelMixin,
#                  mixins.ListModelMixin):
#     def post(self, request):
#         created = request.data.get('created',"")
#         start = request.data.get('start',"")
#         end = request.data.get('end',"")
#         status = request.data.get('status',"")
#         stretch = request.data.get('stretch',"")
#         user_email = request.data.get('user_email',"")
#
#         cure = Cure.objects.create(
#             created= created,
#             start=start,
#             end=end,
#             status=status,
#             stretch=stretch,
#             user_email=user_email
#         )
#         return Response(dict(msg="스트레칭log 생성 완료", name=cure.created, start_date=cure.start.strftime('%Y-%m-%d'), end_date=cure.created))
#
# # Select this user stretchLogs

class CureCreate(APIView):
    def post(self,request):
        user_email = request.data.get('user_email','')
        end_time = request.data.get('end_date',None)
        stretch_num = request.data.get('stnum',0)
        status = request.data.get('status',0)

        cure = Cure.objects.create(user_email=user_email, end=end_time, stretch=stretch_num, status=status )
        
        return Response(dict(msg="cure 생성 완료",end_time=cure.end, start_time=cure.start,
                             date=cure.created, status= cure.status, stretch_num= cure.stretch))

class CureSelect(APIView):
    def post(self, request):
        user_email = request.data.get('user_email', "")

        cures = Cure.objects.filter(user_email=user_email)
        cure_list = []
        for cure in cures:
            cure_list.append(dict(user_email=cure.email, start_time=cure.start, end_time=cure.end, state=cure.state,stretch=cure.stretch, created=cure.created))

        return Response(dict(cures=cure_list))

# Select today's stretchLogs
class TodaySelect(APIView):
    def get(self, request):
        today = datetime.date
        user_email = request.data.get('user_email', "")

        cures = Cure.objects.filter(created=today,user_email=user_email)
        cure_list = []
        for cure in cures:
            cure_list.append(dict(user_email=cure.email, start_time=cure.start, end_time=cure.end, state=cure.state,stretch=cure.stretch, created=cure.created))

        serializers = CureSerializer(cure_list, many=True)
        return Response(serializers.data)

class CureAll(APIView):
    def get(self, request):
        all = Cure.objects.all()
        serializers = CureSerializer(all, many=True)
        return Response(serializers.data)