from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.



def index_formation(request):
	return HttpResponse("here index of formation ")
