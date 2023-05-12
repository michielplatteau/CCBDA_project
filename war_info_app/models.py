from datetime import datetime

from django.db import models
from django.utils import timezone


# Create your models here.
# class TestModel(models.Model):
#     model_field = models.CharField(max_length=30)
#     date = models.DateTimeField(default=datetime.now)


# class TestModel2(models.Model):
#     count = models.IntegerField()
#     name = models.CharField(max_length=30)


class TestModel3(models.Model):
    name = models.CharField(max_length=30)
    date = models.DateTimeField(default=timezone.now)
    tanks = models.IntegerField()
    fuel = models.IntegerField()
