from django.shortcuts import render
from django.http import HttpResponse
from .models import vconferencia


# Create your views here.

def homepage(request):
    return HttpResponse("Helo word")

