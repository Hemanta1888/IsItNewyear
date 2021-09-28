from django.http import HttpResponse
from django.shortcuts import render

import datetime

today = datetime.datetime.now()
def newyear(object):
    return render(object,'newyear.html',{
        "newyear": today.month == 1 and today.day == 1
    })

