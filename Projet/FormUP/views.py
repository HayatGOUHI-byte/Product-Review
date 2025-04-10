from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import *


# Create your views here.



def index_formation(request):
	return HttpResponse("here index of formation ")


def all_formations(request):
	all_formations = Formation.objects.all()
	return render(request, 'all_formations.html', {'all_formations':all_formations})

def tous_cours(request):
	cours = Cours.objects.all()
	return render(request,'tous_cours.html', {'cours': cours})

def ajouter_formation(request):
	if request.method == 'POST':
		form = FormationForm(request.POST)
		if form.is_valid():
			formation = form.save()
			return redirect('all_formations')
	else:
		form = FormationForm()
	return render(request, 'ajouter_formation.html', {'form':form})

def formations_user_specific(request):
	if request.user.is_authenticated :
		try:
			formateur = Formateur.objects.get(user=request.user)
			all_formations = Formation.objects.filter(formateur= formateur).distinct()
			json_message = 'les informations sont recupere avec success!'
			return render(request,'formations_user_specific.html', {
				'all_formations':all_formations,
				'json_message':json_message
				})
		except Formateur.DoesNotExist:
			return HttpResponse('aucun formateur trouvé!')
	else:
		return HttpResponse('le formateur ne st connecte')