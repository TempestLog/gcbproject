from django.db import models
from datetime import date, time

# Create your models here.
class Workers(models.Model):
    date = models.DateField (default=date.now, blank=True)
    time = models.TimeField(max_length=100)
    arrivaltime = models.TimeField(auto_now=False)