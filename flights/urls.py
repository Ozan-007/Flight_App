from django.urls import path

from flights.views import FlightView

urlpatterns = [
    path('flights/', FlightView.as_view(), name='Flight List'),
]
