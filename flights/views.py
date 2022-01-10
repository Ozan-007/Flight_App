from django.shortcuts import render

from flights.serializers import FlightSerializer
from .models import Flight
from rest_framework.permissions import IsAdminUser
from rest_framework import generics, viewsets
# Create your views here.

class FlightListView(viewsets.ModelViewSet):
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer