from django.shortcuts import render
from django.urls import reverse
from django.views.generic import *

from main.forms import *
from main.models import *


class MainPageView(ListView):
    model = Category
    template_name = 'base.html'
    context_object_name = 'categories'



class DishCreateView(CreateView):
    model = Dish
    template_name = 'create_dish.html'
    form_class = CreateDishForm
    context_object_name = 'dish_form'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['dish_form'] = self.get_form(self.get_form_class())
        return context

    def get_success_url(self):
        return reverse('home')


class DishUpdateView(UpdateView):
    model = Dish
    template_name = 'update_dish.html'
    form_class = UpdateDishForm
    pk_url_kwarg = 'id'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['dish_form'] = self.get_form(self.get_form_class())
        return context


class DishDeleteView(DeleteView):
    model = Dish
    template_name = 'delete_dish.html'
    pk_url_kwarg = 'id'

    def get_success_url(self):
        return reverse('home')


class AddReview(View):

    def dish(self, request, pk):
        form = ReviewForm(request.POST)
        dish = Dish.objects.get(id=pk)
        if form.is_valid():
            form = form.save(commit=False)
            form.dish = dish
            form.save()
        return redirect(dish.get_absolute_url())
