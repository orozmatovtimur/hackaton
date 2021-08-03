from django.urls import path
from . import views

urlpatterns = [
    path("", views.register_request, name="register"),
    # path('login/', SignInView.as_view(), name='login'),
    # path('logout/', LogoutView.as_view(), name='logout'),
]