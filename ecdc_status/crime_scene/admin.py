from django.contrib import admin
from .models import CrimeScene

@admin.register(CrimeScene)
class CrimeSceneAdmin(admin.ModelAdmin):
    list_display = ("id", "Name", "UpdatedTime")
    