# Generated by Django 4.2.1 on 2023-05-25 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('war_info_app', '0005_alter_equipment_greatest_losses_direction'),
    ]

    operations = [
        migrations.AlterField(
            model_name='equipmentprediction',
            name='aircraft',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='equipmentprediction',
            name='aircraft_lower',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='equipmentprediction',
            name='aircraft_upper',
            field=models.FloatField(),
        ),
    ]