from django.core.management.base import BaseCommand, CommandError
from crime_scene.models import CrimeScene
from subprocess import call, run
import subprocess
import shutil
from django.utils import timezone

class Command(BaseCommand):
    help = 'Updates the crime scene data in the database'

    def handle(self, *args, **options):
        AllCrimeScenes = CrimeScene.objects.all()
        for Scene in AllCrimeScenes:
            call(["git", "clone", Scene.RepoURL, "--", "current_repo"])
            
            logresult = run(["git", "--git-dir", "current_repo/.git", "log", "--pretty=format:'[%h] %an %ad %s'", "--date=short", "--numstat"], stdout=subprocess.PIPE)
            import json
            from data_miner import DataMiner
            from lines_of_code_extractor import LinesOfCodeExtractor
            from hotspot_compiler import create_hotspots
            from structure_generator import generate_structure
            
            loc = LinesOfCodeExtractor().get_lines_of_code_for_directory("current_repo/")
            commits = DataMiner().extract_changes_per_file(logresult.stdout.decode("utf-8"))
            hotspots = create_hotspots(commits, loc)
            
            structure = generate_structure(hotspots)
            
            Scene.CrimeSceneData = json.dumps(structure)
            Scene.UpdatedTime = timezone.now()
            Scene.save()
            shutil.rmtree("current_repo")

