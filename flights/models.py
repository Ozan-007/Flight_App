from django.db import models

# Create your models here.
class Flight(models.Model):
    flight_number = models.IntegerField()
    airline = models.CharField(max_length=250)
    departure_city = models.CharField(max_length=250)
    arrival_city = models.CharField(max_length=250)
    departure_date = models.DateField()
    estimatedTimeofDeparture = models.TimeField()

    def __str__(self):
        return self.departure_city + " " + self.arrival_city + " " + self.flight_number 


class Passenger(models.Model):
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    email = models.EmailField()
    phone_number = models.IntegerField
    updated_date = models.DateTimeField(auto_now=True)
    created_date = models.DateTimeField(auto_now_add= True)


    def __str__(self):
        return f"{self.first_name} - {self.last_name}"
    