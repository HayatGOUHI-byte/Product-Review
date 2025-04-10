from django import forms
from .models import *

class FormationForm(forms.ModelForm):
	class Meta:
		model =  Formation
		fields = ['titre', 'date_debut', 'date_fin', 'formateur', 'cours']
		widgets = {
		'date_debut' : forms.DateTimeInput(attrs={'type': 'datetime-local'}),
		'date_fin': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
		'formateur': forms.CheckboxSelectMultiple,
		'cours': forms.CheckboxSelectMultiple,
		}