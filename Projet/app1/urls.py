from django.urls import path
from . import views


urlpatterns = [
path('accueil/',views.home, name='home'),



#toutes les routes en relation avec le restaurant

path('', views.restaurant_list, name='restaurant_list'),
path('add/', views.restaurant_create, name='restaurant_create'),
path('<int:pk>/edit/', views.RestaurantUpdateView.as_view(), name='restaurant_update'),
path('<int:pk>/delete/', views.restaurant_delete, name='restaurant_delete'),

]



