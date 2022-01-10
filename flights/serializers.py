from django.db.models import fields
from rest_framework import serializers
from .models import Reservation,Flight,Passenger

#Serializers

class FlightSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flight
        fields = "__all__"


class PassengerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Passenger
        fields = "__all__"


class ReservationSerializer(serializers.ModelSerializer):
        passenger = PassengerSerializer(many=True, required=False)
        flight_id = serializers.IntegerField()
        user = serializers.StringRelatedField()
        user_id = serializers.IntegerField(required=False, write_only=True)        
        class Meta:
            model = Reservation
            fields = ("id", "flight_id","passenger","user","user_id")


