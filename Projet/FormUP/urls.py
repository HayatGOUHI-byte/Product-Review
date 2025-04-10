from django.urls import path
from . import views


urlpatterns = [
path('',views.index_formation, name='index_formation'),
path('all_formations/',views.all_formations, name='all_formations'),

]
