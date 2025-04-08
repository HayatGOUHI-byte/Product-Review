from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import *
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from django.views.generic.list import ListView
from django.urls import reverse_lazy


def home(request):
    return render(request,'index.html')


def restaurant_list(request):
    restaurants = Restaurant.objects.all()
    return render(request,'restaurants/index.html', {'restaurants':restaurants})


def restaurant_create(request):
    form = RestaurantForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('restaurant_list')
    return render(request, 'restaurants/form.html', {'form': form})


class RestaurantUpdateView(UpdateView):
    model = Restaurant
    form_class = RestaurantForm
    template_name = 'restaurants/form_update.html'
    context_object_name = 'restaurant'

    def form_valid(self,form):
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('restaurant_list')



def restaurant_delete(request):
    pass


#les vues et les classes en relation avec dishes

class DishListView(ListView):
    model = Dish
    template_name = 'restaurants/dish_list.html'
    context_object_name = 'dishes'


class DishCreateView(CreateView):
    model = Dish
    form_class = DishForm
    template_name='restaurants/dish_form.html'

    def form_valid(self, form):
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('dish_list')


class DishUpdateView(UpdateView):
    model =Dish 
    form_class = DishForm
    template_name='restaurants/dish_form.html'

    def get_success_url(self):
        return reverse_lazy('dish_list')



class DishDeleteView(DeleteView):
    model = Dish
    template_name = 'restaurants/dish_confirm_delete.html'
    context_object_name = 'dish'


    def get_success_url(self):
        return reverse_lazy('dish_list')



def plats_par_restaurant(request):
    dishes = Dish.objects.select_related('restaurant').all()
    return render(request,'restaurants/plat.html', {'dishes':dishes})



def submit_review(request, restaurant_id):
    restaurant = Restaurant.objects.get(id=restaurant_id)


    if request.method == 'POST':
        form = ReviewForm(request.POST)

        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.restaurant = restaurant
            review.save()
            return HttpResponse("Votre avis a été ajouté avec succès!")
    else:
        form = ReviewForm()
    return render(request, 'restaurants/submit_review.html', {'form':form, 'restaurant': restaurant})




#2. Avis pour un restaurant spécifique

def avis_restaurant_Specific(request, id):
    restaurant = Restaurant.objects.get(id = id)
    reviews = Review.objects.filter(restaurant = restaurant)

    return render(request, 'restaurants/avis_restaurant_Specific.html', {'reviews':reviews})


#tous les avis d'un utilisateur spécifiQue

def avis_user(request, nom):
    user = User.objects.get(username=nom)
    Review_By_User = Review.objects.filter(user=user)
    return render(request, 'restaurants/Review_By_User.html', {'Review_By_User': Review_By_User})
