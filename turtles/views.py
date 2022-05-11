from django.shortcuts import render

# Create your views here.
# login/views.py

from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Turtle
from django.contrib.auth.hashers import make_password, check_password

from .serializers import TurtleSerializer

# 거북이 가져오기
class TurtleLogin(APIView):
    def get(self, request):
        user_email = request.data.get('user_email',"")
        user = Turtle.objects.filter(email=user_email).first()
        data = dict(
            user_email=user.email,
            user_name=user.name,
            num=user.num
        )
        return Response(data)

# 사용자 거북이 생성
class CreateTurtle(APIView):
    def post(self, request):
        serializer = TurtleSerializer(request.data)

        if Turtle.objects.filter(email=serializer.data['email']).exists():
            # DB에 있는 값 출력할 때 어떻게 나오는지 보려고 user 객체에 담음
            user = Turtle.objects.filter(email=serializer.data['email']).first()
            data = dict(
                msg="이미 존재하는 이메일입니다.",
                user_email=user.email,
                user_name=user.name,
                num=user.num
            )
            return Response(data)
        turtle = serializer.create(request.data)

        return Response(data=TurtleSerializer(turtle).data)