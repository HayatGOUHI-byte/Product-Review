from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Statut(models.Model):
	nom = models.CharField(max_length = 30)

	def __str__(self):
		return self.nom 


class Voiture(models.Model):
	numero_immatriculation = models.CharField(max_length = 9)
	marque = models.CharField(max_length = 20)
	model = models.CharField(max_length = 30)
	annee = models.CharField(max_length = 5)
	kilometrage = models.IntegerField()
	statut = models.ForeignKey(Statut, on_delete=models.CASCADE, related_name='statut')

	def __str__(self):
		return self.marque


class Permis_Conduite(models.Model):
	titre = models.CharField(max_length=3)

	def __str__(self):
		return self.titre

class Client(models.Model):
	nom = models.CharField(max_length = 20)
	prenom = models.CharField(max_length = 20)
	email  =models.CharField(max_length = 50)
	permis_conduite = models.OneToOneField(Permis_Conduite, on_delete=models.CASCADE, related_name='permis')


	def __str__(self):
		return self.nom