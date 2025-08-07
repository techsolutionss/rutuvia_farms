
from django.urls import path
from .views import ProductListView


app_name = "product"

urlpatterns = [
    path("products/", view=ProductListView.as_view(), name="products")
]