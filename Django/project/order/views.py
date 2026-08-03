from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def orderlist(request):
    return HttpResponse("I am in Order App")