from django.db import models

# Create your models here.

class Provider(models.Model):
    p_name = models.CharField(blank=False, null=False, max_length=50)
    p_email = models.EmailField(blank=False, null=False)
    car_name = models.CharField(max_length=50)
    seats_available = models.IntegerField(default=3)

class Receiver(models.Model):
    r_name = models.CharField(blank=False, null=False, max_length=50)
    r_email = models.EmailField(blank=False, null=False)
    