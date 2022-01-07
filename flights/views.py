from django.shortcuts import render

from flights.serializers import FlightSerializer
from .models import Flight
from rest_framework.permissions import IsAdminUser
from rest_framework import generics
# Create your views here.

class FlightView(generics.ListCreateAPIView):
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer