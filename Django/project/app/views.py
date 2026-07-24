from django.shortcuts import render
from django.http import HttpResponse
from datetime import date

# Create your views here.
def home(request):
    return render(request,"home.html")

def contact(request):
    return HttpResponse("Hello World")

def about(request):
    info={
        'name':'apple',
        "color":"Green",
        "price":120,
        "origin":['kashmir','chennai'],
        "Reached":date(2026,7,23)
    }
    return render(request,"about.html",info)