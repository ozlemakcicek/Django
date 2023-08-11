from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Flight(models.Model):
    flight_number=models.CharField(max_length=10)
    operation_airlines=models.CharField(max_length=100)
    departure_city=models.CharField(max_length=30)
    arrival_city=models.CharField(max_length=30)
    date_departure=models.DateTimeField()
    estimated_time=models.TimeField()

    def __str__(self):
        return f"{self.flight_number} - {self.departure_city}- {self.arrival_city}"
    
class Passenger(models.Model):
    first_name=models.CharField(max_length=30)
    last_name=models.CharField(max_length=30)
    email=models.EmailField()
    phone_number=models.IntegerField()
    create_date=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.first_name} - {self.last_name}"

class Reservation(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    flight=models.ForeignKey(Flight,on_delete=models.CASCADE,related_name="reservations")
    passenger=models.ManyToManyField(Passenger,related_name="reservation")

    def __str__(self):
        return f"{self.user} - {self.flight}"