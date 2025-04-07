from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Restaurant
from .forms import RestaurantForm
from django.views.generic.edit import UpdateView
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