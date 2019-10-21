from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.admin.views.decorators import staff_member_required
from .models import Cafe, Dish, Order, OrderDetail
from django.views.generic.list import ListView



class CafeListView(ListView):
    model = Cafe
    paginate_by = 100

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):        
        return super(CafeListView, self).dispatch(request, *args, **kwargs)


class DishListView(ListView):
    model = Dish
    template_name = 'core/dishes.html'

    def get_queryset(self):
        print(self.kwargs)
        context = Dish.objects.filter(cafe=self.kwargs['id'])
        return context

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):        
        return super(DishListView, self).dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return DishListView.as_view()(request)


class CartListView(ListView):
    model = Dish
    template_name = 'core/cart.html'

    def get_queryset(self):
        print(self.kwargs)
        context = Dish.objects.all()
        return context
    
    def post(self, request, *args, **kwargs):
        ids = request.POST.getlist('dish_cart')
        print(ids)
        qs = Dish.objects.filter(id__in=ids)
        # print(self.qs, qs)
        # stuff = Dish.filter(id__in=stuff)
        return render(request, self.template_name, {'objects_list': qs})

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):        
        return super(DishListView, self).dispatch(request, *args, **kwargs)


@login_required
def create_order(request):
    dishes = request.POST.getlist('dish_cart')
    print('CREATE', dishes)
    new_order = Order()