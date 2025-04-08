from django.db import models

# Create your models here.




class Livre(models.Model):
	titre = models.CharField(max_length=100)
	author  = models.CharField(max_length=100)
	prix = models.IntegerField()


	def __str__self(self):
		return self.titre