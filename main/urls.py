<<<<<<< HEAD
=======

>>>>>>> bakay
from django.urls import path

from .views import *

urlpatterns = [
    path('home/', MainPageView.as_view(), name='home'),
    path('dish/create/', DishCreateView.as_view(), name='create_dish'),
    path('dish/update/<int:id>/', DishUpdateView.as_view(), name='update_dish'),
    path('dish/delete/<int:id>/', DishDeleteView.as_view(), name='delete_dish'),

<<<<<<< HEAD
]
=======
    # cart urls
    path('cart/add/<int:id>/', cart_add, name='cart_add'),
    path('cart/item_clear/<int:id>/', item_clear, name='item_clear'),
    path('cart/item_increment/<int:id>/',
         item_increment, name='item_increment'),
    path('cart/item_decrement/<int:id>/',
         item_decrement, name='item_decrement'),
    path('cart/cart_clear/', cart_clear, name='cart_clear'),
    path('cart/cart-detail/', cart_detail, name='cart_detail'),
    ]

# from django.contrib import admin
# from django.urls import path, include
#

# from django.contrib import admin
# from django.urls import path, include


# urlpatterns = [
#     path('/', )

>>>>>>> bakay

