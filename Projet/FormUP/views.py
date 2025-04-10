from django.shortcuts import render
from django.http import HttpResponse
from .models import *


# Create your views here.



def index_formation(request):
	return HttpResponse("here index of formation ")


def all_formations(request):
	all_formations = Formation.objects.all()
	return render(request, 'all_formations.html', {'all_formations':all_formations})

def tous_cours(request):
	cours = Cours.objects.all()
	return render(request,'tous_cours.html', {'cours': cours})