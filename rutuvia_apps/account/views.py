from django.shortcuts import render, redirect
from .models import Account
from django.contrib import messages
from .forms import AccountForm, LoginForm
from django.http import HttpResponseNotAllowed
from .auth import user_authenticate, user_login, user_is_authenticated

def create_user_account(request):
    if request.method == "POST":
        context = {}
        form = AccountForm(request.POST)
        if form.is_valid():
            account = Account(
                firstname = form.cleaned_data["firstname"],
                lastname = form.cleaned_data["lastname"],
                email = form.cleaned_data["email"],
                phone = form.cleaned_data["phone"],
                password = form.cleaned_data["password"]
            )
            account.save()
            return redirect("account:login")
        else:
            context["form"] = form
            messages.error(request,"the form is not valid")
            return render(request, "account/create_account.html", context=context)
    elif request.method == "GET":
        context = {}
        context["form"] = AccountForm()
        return render(request, "account/create_account.html", context=context)
    else:
        return HttpResponseNotAllowed(["GET", "POST"])

def login(request):
    if request.method == "POST":
        context = {}
        form = LoginForm(request.POST)
        if form.is_valid():
            user = user_authenticate(form.cleaned_data)
            if user:
                user_login(request, user)
                messages.success(request, "login successful")
            else:
                messages.error(request, "email or password does not exist")
            return redirect("account:login")
        else:
            context["form"] = form
            return render(request, "account/login.html", context=context)
    elif request.method == "GET":
        print(user_is_authenticated(request))
        context = {}
        context["form"] = LoginForm()
        return render(request, "account/login.html", context=context)
    else: 
        return HttpResponseNotAllowed(["GET", "POST"])
    