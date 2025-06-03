from django.contrib import admin
from .models import Contact


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ("pk", "email", "fullname", "phone", "subject", "created_at")
    search_fields = ("email",)