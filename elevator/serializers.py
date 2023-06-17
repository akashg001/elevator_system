from rest_framework import serializers
from home.models import Elevator

class ElevatorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Elevator
        fields = '__all__'
