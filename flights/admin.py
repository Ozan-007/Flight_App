from django.contrib import admin

from flights.models import Flight, Passenger

# Register your models here.
admin.site.register(Flight)
admin.site.register(Passenger)