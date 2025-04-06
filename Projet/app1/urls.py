from django.urls import path
from . import views


urlpatterns = [
path('accueil/',views.home, name='home'),



#toutes les routes en relation avec le restaurant

path('index', views.index, name='index'),

]



