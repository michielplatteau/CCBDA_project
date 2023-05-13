import os
from datetime import datetime, timedelta


from django.http import HttpResponse
from django.shortcuts import render
from django.utils import timezone


from war_info_app.models import TestModel3
from war_info_app.models import Kills



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


def index(request):

    # Clear data from previous runs
    TestModel3.objects.all().delete()

    # Add some data for testing
    tm = TestModel3(name='test_name', tanks=10, fuel=1, date=timezone.now() - timedelta(days=1))
    tm.save()
    tm1 = TestModel3(name='test_name1', tanks=20, fuel=7, date=timezone.now() - timedelta(days=2))
    tm1.save()
    tm2 = TestModel3(name='test_name2', tanks=25, fuel=2, date=timezone.now() - timedelta(days=11))
    tm2.save()

    response = TestModel3.objects.all()
    data = []
    for x in response:
        data.append([str(x.date)[:10], x.tanks, x.fuel])
    print(data)

    # unpack dict keys / values into two lists
    dates, tanks, fuel = zip(*data)

    context = {
        "dates": dates,
        "tanks": tanks,
        "fuel": fuel,
    }
    return render(request, "index.html", context)


def index2(request):

    response = Kills.objects.all()
    data = []
    for x in response:
        data.append([str(x.date)[:10], x.losses])
    # print(data)

    # unpack dict keys / values into two lists
    dates, losses = zip(*data)

    context = {
        "dates": dates,
        "losses": losses,
    }
    return render(request, "index.html", context)
