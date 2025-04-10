from django.contrib import admin
from .models import *

class FormationAdmin(admin.ModelAdmin):
    list_display = ('titre', 'date_debut', 'date_fin')  # Affiche les colonnes dans la liste des formations
    filter_horizontal = ('formateur', 'cours')  # Ajoute une interface de sélection facile avec deux listes

admin.site.register(Formation, FormationAdmin)
admin.site.register(Formateur)
admin.site.register(Cours)
