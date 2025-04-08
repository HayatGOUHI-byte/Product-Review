from django.shortcuts import render, redirect
from .models import Livre,Emprunt
# Create your views here.
from django.utils import timezone


def livre_disponible(request):
	livres = Livre.objects.all()
	return render(request,'biblios/home.html',{'livres':livres})


#ajouter une nouvelle emprunt
def add_emprunt(request, id ):
	livre = Livre.objects.get(id = id)
	if request.method == 'GET':
		Emprunt.objects.create (
		livre=livre,
		user = request.user,
		Emprunt_at=timezone.now()
		)
		livre.disponible=False
		livre.save()
		return redirect('livre_disponible')  # ou la page de ton choix
	else:
		return redirect('livre_disponible')
