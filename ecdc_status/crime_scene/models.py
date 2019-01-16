from django.db import models

class CrimeScene(models.Model):
    Name = models.CharField(max_length = 2000)
    RepoURL = models.URLField()
    UpdatedTime = models.DateTimeField("Time of last update", null = True)
    CrimeSceneData = models.TextField("Crime scene JSON data", blank = True)
