from django.shortcuts import render
from django.urls import reverse
from django.views.generic import *
from django.contrib.auth.decorators import login_required


from main.forms import *
from main.models import *


class MainPageView(ListView):
    model = Category
    template_name = 'base.html'
    context_object_name = 'categories'


class DishListView(ListView):
    model = Dish
    template_name = 'list_dish.html'
    context_object_name = 'dishes'

    def get_queryset(self):
        queryset = super().get_queryset()
        slug = self.kwargs.get('slug')
        queryset = queryset.filter(category__slug=slug)
        return queryset

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = self.kwargs.get('slug')
        return context


class DishDetailView(DetailView):
    model = Dish
    template_name = 'detail_dish.html'
    context_object_name = 'dishess'
    pk_url_kwarg = 'id'


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

    def get_success_url(self):
        return reverse('home')


class DishDeleteView(DeleteView):
    model = Dish
    template_name = 'delete_dish.html'
    pk_url_kwarg = 'id'

    def get_success_url(self):
        return reverse('home')


# class AddReview(View):
#
#     def dish(self, request, pk):
#         form = ReviewForm(request.POST)
#         dish = Dish.objects.get(id=pk)
#         if form.is_valid():
#             form = form.save(commit=False)
#             form.dish = dish
#             form.save()
#         return redirect(dish.get_absolute_url())


@login_required()
def cart_add(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect("home")


@login_required()
def item_clear(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.remove(product)
    return redirect("cart_detail")


@login_required()
def item_increment(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect("cart_detail")


@login_required()
def item_decrement(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.decrement(product=product)
    return redirect("cart_detail")


@login_required()
def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    return redirect("cart_detail")


@login_required()
def cart_detail(request):
    return render(request, 'cart/cart_detail.html')
