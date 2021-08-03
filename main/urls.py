<<<<<<< HEAD
from django.urls import path

from main.views import *

urlpatterns = [
    path('', MainPageView.as_view(), name='home'),
    path('dish/create/', DishCreateView.as_view(), name='create_dish'),
    path('dish/update/<int:id>/', DishUpdateView.as_view(), name='update_dish'),
    path('dish/delete/<int:id>/', DishDeleteView.as_view(), name='delete_dish'),

# from django.contrib import admin
# from django.urls import path, include
#
=======
from django.contrib import admin
from django.urls import path, include

>>>>>>> timur
# urlpatterns = [
#     path('/', )
]

