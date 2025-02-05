from django.shortcuts import render
from django.http import HttpResponse
from datetime import date
from . import skibidi
# Create your views here.

def index(request):
    return render(request, "czyniedziela/index.html",{
        "information": skibidi.isTradingSunday()
    })