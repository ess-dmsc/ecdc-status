from django.urls import path

from . import views

urlpatterns = [
    path('random/', views.random_crime_scene),
    path('<int:id>/', views.crime_scene),
    path('data/<int:id>', views.crime_scene_data, name="crime_scene_data"),
]