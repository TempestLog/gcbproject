from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

# Create your models here.
class Workers(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    arrivaltime = models.TimeField()

class Dates(models.Model):
    workday = models.DateField(default=datetime.today)
    start_time = models.TimeField()
    employee = models.ManyToManyField(Workers, blank=True)
