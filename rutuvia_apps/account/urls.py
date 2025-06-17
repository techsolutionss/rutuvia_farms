from django.urls import path
from .views import create_user_account, login

app_name = "account"

urlpatterns = [
    path("create/account/", view=create_user_account, name="create_user"),
    path("login/", view=login, name="login")
]