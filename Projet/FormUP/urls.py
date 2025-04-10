from django.urls import path
from . import views


urlpatterns = [
path('',views.index_formation, name='index_formation'),
path('all_formations/',views.all_formations, name='all_formations'),
path('tous_cours/', views.tous_cours, name='tous_cours.html'),
path('ajouter_formation/', views.ajouter_formation, name='ajouter_formation'),
path('formations_user_specific/', views.formations_user_specific, name='formations_user_specific'),
]
