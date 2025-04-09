from django.db import models
from django.contrib.auth.models import User





class Livre(models.Model):
	titre = models.CharField(max_length=100)
	author  = models.CharField(max_length=100)
	prix = models.IntegerField()
	disponible = models.BooleanField(default=True)

	def __str__(self):
		return self.titre


class Emprunt(models.Model):
	livre = models.ForeignKey(Livre, on_delete=models.CASCADE, related_name='emprunts')
	user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='emprunts')
	avis = models.CharField(max_length=100)
	Emprunt_at = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return f"{self.user.username} a emprunté {self.livre.titre}"

