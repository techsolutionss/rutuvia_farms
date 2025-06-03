from django import forms
from .models import Contact

class ContactForm(forms.Form):
    fullname = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Full Name"})
    )
    email = forms.EmailField(
        max_length=50,
        widget=forms.EmailInput(attrs={"class": "form-control", "placeholder": "Email Address"})
    )
    phone = forms.CharField(
        max_length=15,
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Phone Number"})
    )
    subject = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Subject"})
    )
    message = forms.CharField(
        widget=forms.Textarea(attrs={"class": "form-control", "rows": 5, "placeholder": "Write Message"})
    )
    def clean(self):
        cleaned_data = super().clean()
        # email = cleaned_data.get("email")
        # if Contact.objects.filter(email=email).exists():
        #     self.add_error("email", "email already exist")
        return cleaned_data 