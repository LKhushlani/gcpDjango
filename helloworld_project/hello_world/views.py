from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def homePage(reuest):
    return HttpResponse("Hello World")
