from django.shortcuts import render
from django.urls import path
from .views import OrdersListView


app_name = "orders"

urlpatterns = [
    path("orders/", view=OrdersListView.as_view(), name="Orders")
]

