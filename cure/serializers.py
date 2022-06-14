from rest_framework import serializers
from .models import Cure

class CureSerializer(serializers.ModelSerializer):

    class Meta:
        model = Cure
        fields = ['id','created','start','end','stretch','status','user_email']
