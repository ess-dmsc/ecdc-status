from django.urls import path

from . import views

urlpatterns = [
    path('', views.random_maxim),
    path('raw/', views.random_raw_maxim),
]