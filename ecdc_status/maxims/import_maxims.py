def add_known_maxims(apps, schema_editor):
    from maxims.models import Maxim
    MaximFile = open("maxims/maxims.txt", "r")
    MaximLines = MaximFile.readlines()
    for Line in MaximLines:
        currentEntry = Maxim(Text=Line)
        currentEntry.save()
