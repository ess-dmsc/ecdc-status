# Generated by Django 2.1.5 on 2019-01-16 14:11

from django.db import migrations, models

def create_entries(apps, schema_editor):
    from crime_scene.models import CrimeScene
    ListOfScenes = [["event-formation-unit", "https://github.com/ess-dmsc/event-formation-unit.git"], ["kafka-to-nexus", "https://github.com/ess-dmsc/kafka-to-nexus.git"], ["forward-epics-to-kafka", "https://github.com/ess-dmsc/forward-epics-to-kafka.git"], ["kafkacow", "https://github.com/ess-dmsc/kafkacow.git"]]
    for Scene in ListOfScenes:
        currentScene = CrimeScene(Name=Scene[0], RepoURL=Scene[1])
        currentScene.save()

class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CrimeScene',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=2000)),
                ('RepoURL', models.URLField()),
                ('UpdatedTime', models.DateTimeField(null=True, verbose_name='Time of last update')),
                ('CrimeSceneData', models.TextField(blank=True, verbose_name='Crime scene JSON data')),
            ],
        ),
        migrations.RunPython(create_entries)
    ]
