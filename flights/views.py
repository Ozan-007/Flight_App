from flights.serializers import FlightSerializer, ReservationSerializer
from .models import Flight, Reservation
from rest_framework.permissions import IsAdminUser
from rest_framework import generics, viewsets , filters
from .permissions import IsStuffOrReadOnly

# Create your views here.

class FlightListView(viewsets.ModelViewSet):
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer
    permission_classes = [IsStuffOrReadOnly,]
    filter_backends =  [filters.SearchFilter]
    search_fields = ["departure_city", 'arrival_city']

class ReservationView(viewsets.ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer


    def get_queryset(self):
        queryset = Reservation.objects.all()
        if self.request.user.is_superuser:
            return queryset
        else:
            return queryset.filter(user=self.request.user)

    
    