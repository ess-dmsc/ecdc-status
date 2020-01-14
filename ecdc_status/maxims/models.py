from django.db import models
from django.utils import timezone

class Maxim(models.Model):
    Id = models.AutoField(primary_key=True)
    CreationDate = models.DateTimeField("Time of addition to database", null = False, default = timezone.now)
    Text = models.TextField(max_length = 2000)
