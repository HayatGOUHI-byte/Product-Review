from django.contrib import admin
from .models import Dish, Review, Restaurant

# Register your models here.


admin.site.register(Restaurant)
admin.site.register(Dish)
admin.site.register(Review)
