from django import forms
from .models import Restaurant, Dish, Review


class RestaurantForm(forms.ModelForm):
	class Meta:
		model = Restaurant
		fields = ['name', 'address','type']



class DishForm(forms.ModelForm):
	class Meta:
		model = Dish
		fields = ['restaurant', 'name', 'description', 'price', 'is_available']

class ReviewForm(forms.ModelForm):
	class Meta:
		model = Review
		fields = ['restaurant', 'rating', 'comment']


		