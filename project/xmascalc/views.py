from django.shortcuts import render
import datetime

# Create your views here.
def xmas(request):
    today= datetime.datetime.now()
    return render(request,'xmascalc/index.html',{
        "xmas": today.month==12 and today.day==25,
        "date": today.date,
        "time": today.time
    })