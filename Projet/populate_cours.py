import os
import django
import random

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mon_projet.settings')  # remplace 'mon_projet' par ton dossier projet
django.setup()

from FormUP.models import Cours

titres = ["Python", "Django", "Data Science", "Machine Learning", "JavaScript", "React", "SQL", "Linux", "Docker", "Git"]
descriptions = [
    "Cours pour débutants", "Cours avancé", "Atelier pratique", "Cours complet",
    "Introduction rapide", "Formation intensive", "Cours en ligne", "Projet guidé"
]

for i in range(30):
    titre = random.choice(titres) + f" {i+1}"
    description = random.choice(descriptions)
    duree = f"{random.randint(1, 10)}h"
    Cours.objects.create(titre=titre, description=description, duree=duree)

print("✅ 30 cours insérés avec succès !")
