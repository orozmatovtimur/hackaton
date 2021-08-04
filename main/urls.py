from django.urls import path

from main.views import *

urlpatterns = [
    path('home/', MainPageView.as_view(), name='home'),
    path('dish/create/', DishCreateView.as_view(), name='create_dish'),
    path('dish/update/<int:id>/', DishUpdateView.as_view(), name='update_dish'),
    path('dish/delete/<int:id>/', DishDeleteView.as_view(), name='delete_dish'),

]

