from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from django.utils import timezone
from .models import Event

def index(request):
    CurrentEvents = Event.objects.exclude(EndDate__isnull = True).filter(EndDate__gte = timezone.now()).filter(StartDate__lt = timezone.now())
    FutureEvents = Event.objects.filter(StartDate__gte = timezone.now())
    template = loader.get_template('upcoming_events.html')
    context = {
        'event_now': len(CurrentEvents) > 0,
        'event_list': FutureEvents.union(CurrentEvents).order_by('StartDate'),
    }
    return HttpResponse(template.render(context, request))
    