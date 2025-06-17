from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib import messages
from django.views.generic.base import TemplateView
from .forms import ContactForm
from .models import Contact, Service

class HomeTemplateView(TemplateView):
    template_name = "pages/index.html"

    def render_to_response(self, context, **kwargs):
        response = super(HomeTemplateView, self).render_to_response(context, **kwargs)
        return response
    
    def get_context_data(self, **kwargs):
        context = super(HomeTemplateView, self).get_context_data(**kwargs)
        return context
    
class CartTemplateView(TemplateView):
    template_name = "pages/cart.html"

    def render_to_response(self, context, **kwargs):
        response = super(CartTemplateView, self).render_to_response(context, **kwargs)
        return response

class AboutTemplateView(TemplateView):
    template_name = "pages/about.html"

    def render_to_response(self, context, **kwargs):
        response = super(AboutTemplateView, self).render_to_response(context, **kwargs)
        return response
    
    def get_context_data(self, **kwargs):
        context = super(AboutTemplateView, self).get_context_data(**kwargs)
        return context
    
class ContactTemplateView(TemplateView):
    template_name = "pages/contact.html"

    def render_to_response(self, context, **kwargs):
        response = super(ContactTemplateView, self).render_to_response(context, **kwargs)
        return response
    
    def get_context_data(self, **kwargs):
        context = super(ContactTemplateView, self).get_context_data(**kwargs)
        context["form"] = ContactForm()
        return context
    
    def post(self, request, *args, **kwargs):
        form = ContactForm(request.POST)
        if form.is_valid(): 
            contact = Contact(**form.cleaned_data)
            contact.save()
            messages.success(request, "Your message has been sent successfully.")
            return redirect("pages:contact")
        else:
            print(form.errors)
            return render(request, "pages/contact.html", {"form": form})
        
class ServicesTemplateView(TemplateView):
    template_name = "pages/services.html"

    def render_to_response(self, context, **kwargs):
        response = super(ServicesTemplateView, self).render_to_response(context, **kwargs)
        return response
    
    def get_context_data(self, **kwargs):
        context = super(ServicesTemplateView, self).get_context_data(**kwargs)
        services = Service.objects.all()
        context["services"] = services
        return context
