# Generated by Django 4.2.1 on 2023-05-05 12:13

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TestModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model_field', models.CharField(max_length=30)),
                ('date', models.DateTimeField(default=datetime.datetime.today)),
            ],
        ),
    ]
