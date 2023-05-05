from datetime import datetime

from django.db import models


# Create your models here.
class TestModel(models.Model):
    model_field = models.CharField(max_length=30)
    date = models.DateTimeField(default=datetime.now)
