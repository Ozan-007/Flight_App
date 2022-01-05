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

        