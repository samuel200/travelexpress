from django.db import models

class Flight(models.Model):
    number = models.IntegerField()
    terminal = models.CharField(max_length=2)
    gate = models.IntegerField()
    departure_time = models.DateTimeField()
    airport = models.CharField(max_length=200)
    flight_class = models.CharField(max_length=50)
    seat_number = models.IntegerField()
    status = models.CharField(max_length=50)
    depart_from = models.CharField(max_length=200)
    destination = models.CharField(max_length=200)

    def __str__(self):
        return str(self.number)