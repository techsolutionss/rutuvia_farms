from django.urls import path
from rutuvia_apps.pages import views

app_name = "pages"

urlpatterns = [
    path("", view=views.HomeTemplateView.as_view(), name="index"),
    path("contact/", view=views.ContactTemplateView.as_view(), name="contact"),
    path("about/", view=views.AboutTemplateView.as_view(), name="about"),
    path("services/", view=views.ServicesTemplateView.as_view(), name="services"),
    path("cart/", view=views.CartTemplateView.as_view(), name="cart")
]           