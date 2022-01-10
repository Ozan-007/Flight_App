from django.urls import path
from rest_framework import routers
from flights.views import FlightListView

router = routers.DefaultRouter()
router.register('flights', FlightListView) 

urlpatterns = [

]

urlpatterns += router.urls
