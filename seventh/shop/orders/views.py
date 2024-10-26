from django.shortcuts import render
from django.views.generic import CreateView
from .forms import OrderForm


class OrderCreateView(CreateView):
    form_class = OrderForm
    template_name = 'orders/order-create.html'
