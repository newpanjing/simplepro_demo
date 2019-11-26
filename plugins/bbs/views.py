from django.http import HttpResponse
import json

from django.shortcuts import render
import datetime


def index(request):
    return render(request, 'hello.html', {
        'date': datetime.datetime.now()
    })


def hello(request):
    return HttpResponse(json.dumps({'a': 'ok'}), content_type='application/json')
