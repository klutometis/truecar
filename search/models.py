from django.db import models

# Create your models here.
class Vehicle(models.Model):
    # These might have been foreign keys.
    make = models.CharField(max_length=255)
    model = models.CharField(max_length=255)
    body = models.CharField(max_length=255)

    # Not sure what this boolean represents.
    flag = models.BooleanField()

    # Might have been a datetime.
    year = models.IntegerField()

    # Might have been an integer; which is how we're supposed to deal
    # with money, frankly.
    MSRP = models.FloatField()
    details = models.CharField(max_length=255)
    image = models.CharField(max_length=255)
