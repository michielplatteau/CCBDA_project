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


class Kills(models.Model):
    date = models.DateField(primary_key=True)
    day = models.IntegerField()
    losses = models.IntegerField()


class EventsMap(models.Model):
    id = models.TextField(primary_key=True)
    date = models.DateField()
    type = models.TextField()
    location = models.TextField()
    latitude = models.FloatField()
    longitude = models.FloatField()
    notes = models.TextField()
    fatalities = models.IntegerField()


class Equipment(models.Model):
    date = models.DateField()
    day = models.IntegerField()
    aircraft = models.IntegerField()
    helicopter = models.IntegerField()
    tank = models.IntegerField()
    apc = models.IntegerField()
    field_artillery = models.IntegerField()
    mrl = models.IntegerField()
    military_auto = models.IntegerField()
    fuel_tank = models.IntegerField()
    drone = models.IntegerField()
    naval_ship = models.IntegerField()
    anti_aircraft_warfare = models.IntegerField()
    special_equipment = models.IntegerField()
    mobile_srbm_system = models.IntegerField()
    greatest_losses_direction = models.TextField()
    vehicles_and_fuel_tanks = models.IntegerField()
    cruise_missiles = models.IntegerField()
    total_air_units = models.IntegerField()
    total_naval_units = models.IntegerField()
    total_ground_units = models.IntegerField()


class EquipmentPrediction(models.Model):
    date = models.DateField()
    aircraft = models.FloatField()
    aircraft_lower = models.FloatField()
    aircraft_upper = models.FloatField()


class EventsMap2(models.Model):
    date = models.DateField()
    latitude = models.FloatField()
    longitude = models.FloatField()
    type = models.TextField()
