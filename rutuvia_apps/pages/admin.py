from django.contrib import admin
from .models import Contact, Service


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ("pk", "email", "fullname", "phone", "subject", "created_at")
    search_fields = ("email",)

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ("pk", "title", "image")
    