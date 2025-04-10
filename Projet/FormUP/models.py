from django.db import models
from django.contrib.auth.models import User


class Cours(models.Model):
    titre = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    duree = models.CharField(max_length=10)

    def __str__(self):
        return self.titre


class Formateur(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    specialite = models.CharField(max_length=100)
    bio = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.user.username

class Formation(models.Model):
	titre = models.CharField(max_length = 100)
	date_debut = models.DateTimeField()
	date_fin = models.DateTimeField()
	formateur = models.ForeignKey(Formateur, on_delete=models.CASCADE, related_name='formations_donnee')
    cours = models.ForeignKey(Cours, on_delete=models.CASCADE, related_name='formations')


    def __str(self):
    	return self.titre 
