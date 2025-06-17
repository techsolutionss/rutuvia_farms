from django import forms
from django.forms import ValidationError
from .models import Account

class AccountForm(forms.Form):
    firstname = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control py-3", "placeholder":"First Name"}))
    lastname = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control py-3", "placeholder":"Last Name"}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={"class":"form-control py-3", "placeholder":"Email"}))
    phone = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control py-3", "placeholder":"Phone"}))
    password = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control py-3", "placeholder":"Password"}))
    confirm_password = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control py-3", "placeholder":"Confirm Password"}))

    def clean(self):
        cleaned_data =  super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")
        email = cleaned_data.get("email")
        phone = cleaned_data.get("phone")
        if password != confirm_password:
            self.add_error("confirm_password", "passwords do not match")
        
        if Account.objects.filter(email=email).exists():
            self.add_error("email", "email already exist")
        
        if Account.objects.filter(phone=phone).exists():
            self.add_error("phone", "phone number already exist")

class LoginForm(forms.Form):
    email = forms.EmailField(label="Email Address", widget=forms.EmailInput(attrs={"class":"form-control"}))
    password = forms.CharField(label="Password", widget=forms.PasswordInput(attrs={"class":"form-control"}))