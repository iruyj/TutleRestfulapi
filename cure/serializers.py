from rest_framework import serializers
from .models import Cure

class CureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cure
        fields = ['created','completed','stretch1','stretch2','stretch3']
