from django.shortcuts import render
from .models import CrimeScene
from django.template import loader
from django.http import HttpResponse
from random import randint

def random_crime_scene(request):
    AllCrimeScenes = CrimeScene.objects.all()
    RandomIndex = randint(0, len(AllCrimeScenes) - 1)
    return crime_scene(request, AllCrimeScenes[RandomIndex].id, True)

def crime_scene(request, id, auto_zoom = False):
    CurrentCrimeScene = CrimeScene.objects.get(id = int(id))
    template = loader.get_template('crime_scene.html')
    context = {
        'scene_title': CurrentCrimeScene.Name,
        'scene_id': int(id),
        'auto_zoom': auto_zoom
    }
    return HttpResponse(template.render(context, request))
    

def crime_scene_data(request, id):
    CurrentCrimeScene = CrimeScene.objects.get(id = int(id))
    return HttpResponse(CurrentCrimeScene.CrimeSceneData)
    