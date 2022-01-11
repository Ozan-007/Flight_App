from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Flight(models.Model):
    flight_number = models.IntegerField()
    airline = models.CharField(max_length=250)
    departure_city = models.CharField(max_length=250)
    arrival_city = models.CharField(max_length=250)
    departure_date = models.DateField()
    estimatedTimeofDeparture = models.TimeField()

    def __str__(self):
        return self.departure_city + " " + self.arrival_city + " " + f"{self.flight_number}" 


class Passenger(models.Model):
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    email = models.EmailField()
    phone_number = models.IntegerField(null=True,blank=True)
    updated_date = models.DateTimeField(auto_now=True)
    created_date = models.DateTimeField(auto_now_add= True)

    def __str__(self):
        return f"{self.first_name} - {self.last_name}"


class Reservation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    passenger = models.ManyToManyField(Passenger, related_name='passenger')
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE, related_name='reservations')


    def __str__(self):
        return f'{self.flight}'

 