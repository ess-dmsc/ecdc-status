from django.shortcuts import render
from random import randint
from .models import Maxim
from django.http import HttpResponse

def random_raw_maxim(request):
    AllMaxims = Maxim.objects.all()
    RandomIndex = randint(0, len(AllMaxims) - 1)
    return raw_maxim(request, AllMaxims[RandomIndex].Id)

def raw_maxim(request, Id):
    CurrentMaxim = Maxim.objects.get(Id= int(Id))
    return HttpResponse("#{}: {}".format(CurrentMaxim.Id, CurrentMaxim.Text))

def random_maxim(request):
    return random_raw_maxim(request)
    