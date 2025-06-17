from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from .models import Product


class ProductListView(ListView):
    model = Product
    template_name = "product/product_list.html"
    # paginate_by = 10
    
    def get_queryset(self):
        queryset = super(ProductListView, self).get_queryset()
        return queryset

    def get_context_data(self, **kwargs):
        context = super(ProductListView, self).get_context_data(**kwargs)
        return context
