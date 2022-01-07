from rest_framework import serializers
from .models import Reservation,Flight,Passenger

#Serializers

class FlightSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flight
        fields = "__all__"

