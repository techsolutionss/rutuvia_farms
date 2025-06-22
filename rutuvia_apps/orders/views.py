
from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from .models import Orders


class OrdersListView(ListView):
    # model = no model created yet
    template_name = "orders/orders.html"
    # paginate_by = 10
    
    def get_queryset(self):
        queryset = super(OrdersListView, self).get_queryset()
        return queryset

    def get_context_data(self, **kwargs):
        context = super(OrdersListView, self).get_context_data(**kwargs)
        return context
