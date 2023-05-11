import os

from django.http import HttpResponse
from django.shortcuts import render

from war_info_app.models import TestModel3


# DEFINE OUR VIEWS HERE
def home(request):
    return HttpResponse('Home page')


def test_model_view(request):

    # Add some data for testing
    tm = TestModel3(name='test_name', tanks=10, fuel=1)
    tm.save()
    tm1 = TestModel3(name='test_name1', tanks=20, fuel=3)
    tm1.save()
    tm2 = TestModel3(name='test_name2', tanks=30, fuel=2)
    tm2.save()

    response = TestModel3.objects.all()
    a = f"{'Name':->20}{'Date':->50}{'Tanks':->10}{'Fuel':->10} <br>"
    for x in response:
        a += f"{x.name:->20}{str(x.date):->50}{str(x.tanks):->10}{str(x.fuel):->10} <br>"
    print(a)
    return HttpResponse(a)
