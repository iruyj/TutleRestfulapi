
from turtles.models import Turtle
from rest_framework import serializers

class TurtleSerializer(serializers.ModelSerializer):
    # stretches = serializers.StringRelatedField(many=True)   # 해당 모델의 str함수가 반환됨
    
    def create(self, **validated_data):
        turtle = Turtle.objects.create(**validated_data)
        return turtle

    def validate(self, attrs):
        return attrs

    class Meta:
        model = Turtle
        fields = ['email','name','num']


