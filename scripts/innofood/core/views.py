from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.admin.views.decorators import staff_member_required

from .forms import RegistrationForm
from .models import Cafe, Dish, Order, OrderDetail
from django.views.generic.list import ListView
from django.contrib.auth import login, logout, authenticate


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

    # @method_decorator(login_required)
    # def dispatch(self, request, *args, **kwargs):        
    #     return super(DishListView, self).dispatch(request, *args, **kwargs)

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

    # @method_decorator(login_required)
    # def dispatch(self, request, *args, **kwargs):        
    #     return super(DishListView, self).dispatch(request, *args, **kwargs)

def index(request):
    return render(request, 'core/landing.html')


def registration_view(request):
    context = {}
    if request.POST:
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('name')
            raw_password = form.cleaned_data.get('password')
            user = authenticate(username=username, passwors= raw_password)
            login(request, user)
            return redirect("cafes")
        else:
            context['registration_form'] = form
    else:
        form = RegistrationForm()
        context['registration_form'] = form
    return render(request, 'registration/register.html', context)


@login_required
def create_order(request):
    print(request.POST)
    dishes = request.POST.getlist('dish_cart')
    address = request.POST.get('destination')
    print('CREATE', dishes, address)
    # order_det = OrderDetail(dishes=)
    # new_order = Order(destination=address)


    return render(request, 'core/order_approved.html')


# MANAGER PART

class ManagerOrders(ListView):

    model = Order
    template_name = 'core/managerActiveOrders.html'

    def get_queryset(self):
        context = Order.objects.filter(visible=True)
        return context


class ManagerOrdersStatus(ListView):

    model = Order
    template_name = 'core/managerConfirmedOrders.html'

    def get(self, request, confirmed=1, *args, **kwargs):
        confirmed = False if confirmed == 0 else True

        qs_status = Order.objects.filter(confirmed=confirmed)
        return render(request, self.template_name, {'qs': qs_status})

    
