from rest_framework import serializers
from .models import Cure

class CureSerializer(serializers.ModelSerializer):
<<<<<<< HEAD
=======
    # turtle = serializers.ReadOnlyField(source='turtle.email')
>>>>>>> 8c65575f1ec594cd526178f81b12089b48b95548

    class Meta:
        model = Cure
        fields = ['id','created','start','end','stretch','status','user_email']
