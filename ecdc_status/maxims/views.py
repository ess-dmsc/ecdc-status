from django.shortcuts import render
from random import randint
from .models import Maxim
from django.http import HttpResponse
from django.template import loader

def random_raw_maxim(request):
    AllMaxims = Maxim.objects.all()
    RandomIndex = randint(0, len(AllMaxims) - 1)
    return raw_maxim(request, AllMaxims[RandomIndex].Id)

def raw_maxim(request, Id):
    CurrentMaxim = Maxim.objects.get(Id= int(Id))
    return HttpResponse("#{}: {}".format(CurrentMaxim.Id, CurrentMaxim.Text))
    
def html_maxim(request, Id):
    CurrentMaxim = Maxim.objects.get(Id= int(Id))
    template = loader.get_template('maxim.html')
    context = {"id": int(Id), "text":CurrentMaxim.Text}
    return HttpResponse(template.render(context, request))

def random_maxim(request):
    AllMaxims = Maxim.objects.all()
    RandomIndex = randint(0, len(AllMaxims) - 1)
    return html_maxim(request, AllMaxims[RandomIndex].Id)
    