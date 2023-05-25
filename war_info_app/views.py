import os
from datetime import datetime, timedelta

import numpy as np
from django.http import HttpResponse
from django.shortcuts import render
from django.utils import timezone
from datetime import datetime, timedelta
from numpy.polynomial import Polynomial

from war_info_app.models import TestModel3, Kills, EventsMap, EventsMap2, Equipment, EquipmentPrediction


# DEFINE OUR VIEWS HERE
def home(request):
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

    return render(request, 'home.html', context)
    # return HttpResponse('Home page')


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


# def index(request):
#     # Clear data from previous runs
#     TestModel3.objects.all().delete()
#
#     # Add some data for testing
#     tm = TestModel3(name='test_name', tanks=10, fuel=1, date=timezone.now() - timedelta(days=1))
#     tm.save()
#     tm1 = TestModel3(name='test_name1', tanks=20, fuel=7, date=timezone.now() - timedelta(days=2))
#     tm1.save()
#     tm2 = TestModel3(name='test_name2', tanks=25, fuel=2, date=timezone.now() - timedelta(days=11))
#     tm2.save()
#
#     response = TestModel3.objects.all()
#     data = []
#     for x in response:
#         data.append([str(x.date)[:10], x.tanks, x.fuel])
#     print(data)
#
#     # unpack dict keys / values into two lists
#     dates, tanks, fuel = zip(*data)
#
#     context = {
#         "dates": dates,
#         "tanks": tanks,
#         "fuel": fuel,
#     }
#     return render(request, "graphs.html", context)


def index2(request):
    # get all rows in table
    all_days = Kills.objects.all().order_by('day')

    data_all_days = []
    for x in all_days:
        data_all_days.append([str(x.date)[:10], x.day, x.losses])

    # unpack dict keys / values into two lists
    dates_all_days, days_all_days, cumulative_losses_all_days = zip(*data_all_days)

    # Get rows of the last 30 days
    month_ago_date = datetime.strptime(dates_all_days[-1], "%Y-%m-%d") - timedelta(days=31)

    last_month = Kills.objects.filter(date__gte=month_ago_date).order_by('day')
    data_last_month = []
    for i in range(len(last_month) - 1):
        data_last_month.append([str(last_month[i + 1].date)[:10], last_month[i + 1].day, last_month[i + 1].losses,
                                last_month[i + 1].losses - last_month[i].losses])

    # unpack dict keys / values into two lists
    dates_last_month, days_last_month, cumulative_losses_last_month, daily_losses_last_month = zip(*data_last_month)

    daily_losses_last_month_for_predict = list(daily_losses_last_month) + ['null'] * 30

    regression_poly = Polynomial.fit(days_last_month, daily_losses_last_month, deg=1)
    n = 14  # number of days to be predicted
    days_predict = list(days_last_month) + list(range(days_all_days[-1] + 1, days_all_days[-1] + n + 1))
    dates_predict = list(dates_last_month) + [
        (datetime.strptime(dates_all_days[-1], "%Y-%m-%d") + timedelta(days=k)).strftime("%Y-%m-%d")
        for k in range(1, n + 1)]
    daily_losses_predict = regression_poly(np.array(days_predict))

    # add points to be added to the map
    # in db entries should include position, date and comment, title and type

    # Get rows of the last 30 days
    actual_month_ago_date = datetime.now() - timedelta(days=30)

    # events of the last 30 days.
    events_result = EventsMap.objects.filter(date__gte=actual_month_ago_date).order_by('date')
    events_data = []
    for x in events_result:
        events_data.append([str(x.date)[:10], x.type, x.location, x.latitude, x.longitude, x.notes, x.fatalities])

    # unpack dict keys / values into two lists
    dates_events, types_events, locations_events, lat_events, long_events, notes_events, fatalities_events = \
        zip(*events_data)

    context = {
        "dates_all_days": dates_all_days,
        # "days_all_days": days_all_days,
        "cumulative_losses_all_days": cumulative_losses_all_days,
        # "dates_last_month": dates_last_month,
        # "days_last_month": days_last_month,
        "daily_losses_last_month_for_predict": daily_losses_last_month_for_predict,
        "dates_predict": dates_predict,
        "daily_losses_predict": daily_losses_predict,
        "dates_events": dates_events,
        "types_events": types_events,
        "locations_events": locations_events,
        "lat_events": lat_events,
        "long_events": long_events,
        "notes_events": notes_events,
        "fatalities_events": fatalities_events,
    }
    return render(request, "index2.html", context)


def index3(request):
    # get all rows in table
    equipment = list(zip(*[[equip.date.strftime('%Y-%m-%d'), equip.aircraft, equip.helicopter, equip.tank, equip.drone] for equip in Equipment.objects.all().order_by('date')]))
    predictions = list(
        zip(*[[pred.date.strftime('%Y-%m-%d'), pred.aircraft] for pred in EquipmentPrediction.objects.all().order_by('date')]))

    events = list(zip(*[[event.date.strftime('%Y-%m-%d'), event.type, event.latitude, event.longitude] for event in
                        EventsMap2.objects.all().order_by('date')]))

    assert equipment[0][-1] < predictions[0][0]

    context = {
        "equipment": list(zip(*equipment)),
        "equipment_dates": equipment[0],
        "equipment_aircraft": equipment[1],
        "equipment_helicopter": equipment[2],
        "equipment_tank": equipment[3],
        "equipment_drone": equipment[4],

        "equipment_prediction": list(zip(*predictions)),
        "equipment_prediction_dates": equipment[0] + predictions[0],
        "equipment_prediction_aircraft": equipment[1] + predictions[1],

        "events_dates": events[0],
        "events_types": events[1],
        "events_latitudes": events[2],
        "events_longitudes": events[3],
    }

    return render(request, "index3.html", context)
