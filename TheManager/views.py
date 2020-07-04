from django.shortcuts import render
from django.http import HttpResponse


def index (request):
    
    return HttpResponse("I am the first index of The Manger")

# Create your views here.
