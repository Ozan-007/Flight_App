from django.shortcuts import render
from rest_framework import permissions

from flights.serializers import FlightSerializer, ReservationSerializer
from .models import Flight, Reservation
from rest_framework.permissions import IsAdminUser
from rest_framework import generics, viewsets
from .permissions import IsStuffOrReadOnly
# Create your views here.

class FlightListView(viewsets.ModelViewSet):
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer
    permission_classes = [IsStuffOrReadOnly,]


class ReservationView(viewsets.ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer


    def get_queryset(self):
        queryset = Reservation.objects.all()
        if self.request.user.is_superuser:
            return queryset
        else:
            return queryset.filter(user=self.request.user)

    
    