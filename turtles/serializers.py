
from turtles.models import Turtle
from rest_framework import serializers

class TurtleSerializer(serializers.ModelSerializer):
    # stretches = serializers.StringRelatedField(many=True)   # 해당 모델의 str함수가 반환됨
    
    def create(self, validated_data):
        turtle = Turtle.objects.create(**validated_data)
        return turtle

    def validate(self, attrs):
        return attrs

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name',instance.name)
        instance.num = validated_data.get('num',instance.num)
        instance.save()
        return instance

    class Meta:
        model = Turtle
        fields = ['email','name','num']


