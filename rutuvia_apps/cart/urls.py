from django.urls import path 
from .views import cart_page

app_name = "cart"

urlpatterns = [
    path("cartitems/", view=cart_page, name="cartitems")
]
