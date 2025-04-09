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


def ses_emprunts_avis(request):
	if request.user.is_authenticated:
		Emprunts = Emprunt.objects.filter(user=request.user)
		avis = Emprunt.objects.filter(user=request.user)
		return render(request, 'biblios/ses_emprunts_avis.html', {'Emprunts': Emprunts, 'avis': avis})

	else:
		return HttpResponse('error dans la récupération des emprunts soit dans l utilisateur soit dans les emprunts')


def livre_emprunte(request):
	livre_empruntes = Livre.objects.filter(disponible=False)
	return render(request, 'biblios/livre_empruntes.html',{'livre_empruntes':livre_empruntes})