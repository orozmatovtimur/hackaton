from django.shortcuts import render
from django.views.generic import ListView

from main.models import *


class MainPageView(ListView):
    model = Dish
    template_name = 'index.html'
    context_object_name = 'recipes'



