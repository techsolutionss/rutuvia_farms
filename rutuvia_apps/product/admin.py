from django.contrib import admin
from .models import Product, ProductCategory

@admin.register(ProductCategory)
class ProductCategoryModelAdmin(admin.ModelAdmin):
    list_display = ["name"]

@admin.register(Product)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ["name", "get_price", "weight_in_kg", "size", "image"]
    search_fields = ["name"]

    def weight_in_kg(self, obj):
        return f"{obj.weight} kg"
    
    def get_price(self, obj):
        return f"N {int(obj.price)}"
