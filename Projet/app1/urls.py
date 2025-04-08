from django.urls import path
from . import views


urlpatterns = [
path('accueil/',views.home, name='home'),



#toutes les routes en relation avec le restaurant

path('', views.restaurant_list, name='restaurant_list'),
path('add/', views.restaurant_create, name='restaurant_create'),
path('<int:pk>/edit/', views.RestaurantUpdateView.as_view(), name='restaurant_update'),
path('<int:pk>/delete/', views.restaurant_delete, name='restaurant_delete'),


path('dishes/', views.DishListView.as_view(), name='dish_list'),
path('dishes/create/', views.DishCreateView.as_view(), name='dish_create'),
path('dishes/<int:pk>/edit/', views.DishUpdateView.as_view(), name='dish_edit'),
path('dishes/<int:pk>/delete/', views.DishDeleteView.as_view(), name='dish_delete'),


#plat par restaurant
path('dishes/plat_par_restaurant/', views.plats_par_restaurant, name='plat_par_restaurant'),
 path('submit_review/<int:restaurant_id>/', views.submit_review, name='submit_review'),

]



