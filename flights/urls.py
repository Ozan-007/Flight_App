from django.urls import path
from rest_framework import routers
from flights.views import FlightListView, ReservationView

router = routers.DefaultRouter()
router.register('flights', FlightListView) 
router.register('reservations', ReservationView)

urlpatterns = [

]

urlpatterns += router.urls
