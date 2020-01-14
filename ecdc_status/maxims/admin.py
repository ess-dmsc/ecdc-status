from django.contrib import admin
from .models import Maxim

@admin.register(Maxim)
class MaximAdmin(admin.ModelAdmin):
    list_display = ("Id", "Text", "CreationDate")
    
