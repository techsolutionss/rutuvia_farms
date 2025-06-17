from django.urls import path 
app_name = "cart"
from .views import cart_page

urlpatterns = [
    path("cartitems/", view=cart_page, name="cartitems")
]
