from django.shortcuts import render
from rest_framework import permissions

from flights.serializers import FlightSerializer
from .models import Flight
from rest_framework.permissions import IsAdminUser
from rest_framework import generics, viewsets
from .permissions import IsStuffOrReadOnly
# Create your views here.

class FlightListView(viewsets.ModelViewSet):
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer
    permission_classes = (IsStuffOrReadOnly,)