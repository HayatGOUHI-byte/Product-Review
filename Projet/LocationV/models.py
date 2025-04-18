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
	permis_conduite = models.ForeignKey(Permis_Conduite, on_delete=models.CASCADE, related_name='permis')


	def __str__(self):
		return self.nom


class Reservation(models.Model):
	client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='clients')
	voiture = models.ForeignKey(Voiture, on_delete=models.CASCADE, related_name='voitures')
	date_debut = models.DateTimeField()
	date_fin = models.DateTimeField()


	contraints = [
	]

	def __str__(self):
		return self.client.prenom


class Paiement(models.Model):
	reservation=models.OneToOneField(Reservation, on_delete=models.CASCADE, related_name='reservations')
	montant = models.IntegerField()
	mode_paiement = models.CharField(max_length = 23)
	date_paiement = models.DateTimeField()
	etat_paiement = models.CharField(max_length = 100)


class Retour(models.Model):
	voiture = models.ForeignKey(Voiture, on_delete=models.CASCADE, related_name = 'voit')
	etat_vehicule = models.CharField(max_length = 50)
	frais_supplementaire = models.TextField()
	kilometrage_final = models.IntegerField()


class Type_Panne(models.Model):
	panne=models.CharField(max_length = 50)

	def __str__(self):
		return self.panne

class Reparation(models.Model):
	voiture=models.ForeignKey(Voiture, on_delete=models.CASCADE, related_name='v')
	description = models.ForeignKey(Type_Panne, on_delete=models.CASCADE, related_name='type_panne')
	date_reparation = models.DateField()
	cout = models.DecimalField(max_digits=10, decimal_places=2)
	reparateur = models.CharField(max_length=100)
	est_terminee = models.BooleanField(default=False)

class test(request):
	pass

class test2(request):
	pass

class changes(request):
	pass