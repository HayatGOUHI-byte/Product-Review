from django.urls import path
from . import views


urlpatterns = [
path('',views.livre_disponible, name='livre_disponible'),
path('home/', views.livre_disponible, name='home'),
path('add_emprunt/<int:id>/', views.add_emprunt, name='add_emprunt'),



]
