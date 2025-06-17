from django.contrib import admin
from .models import Account

@admin.register(Account)
class AccountModelAdmin(admin.ModelAdmin):
    list_display = ["pk", "firstname", "lastname", "email", "phone", "active", "created_at"]
