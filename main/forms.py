from django import forms

from .models import *


class CreateDishForm(forms.ModelForm):
    class Meta:
        model = Dish
        fields = "__all__"


class UpdateDishForm(forms.ModelForm):
    class Meta:
        model = Dish
        fields = "__all__"