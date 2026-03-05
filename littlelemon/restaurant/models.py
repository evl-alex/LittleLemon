from django.db import models
from django.core.validators import MaxValueValidator


class Booking(models.Model):
    name = models.CharField(max_length=255)
    no_of_guests = models.SmallIntegerField(validators=[MaxValueValidator(999999)])
    booking_date = models.DateTimeField()


class Menu(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    invertory = models.IntegerField(validators=[MaxValueValidator(99999)])
