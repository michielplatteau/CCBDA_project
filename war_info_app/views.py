import os

from django.http import HttpResponse
from django.shortcuts import render

from war_info_app.models import TestModel


# DEFINE OUR VIEWS HERE
def home(request):
    return HttpResponse('Home page')


def test_model_view(request):
    tm = TestModel(model_field='Model field value')
    tm.save()
    response = TestModel.objects.all()
    a = ""
    for x in response:
        a += x.model_field
        a += '; '
        a += str(x.date)
        a += '<br>'
    return HttpResponse(a)
