from django.db import models

class ProductCategory(models.Model):
    name = models.CharField(max_length=50, verbose_name="Product Category")

    def __str__(self):
        return self.name

class Product(models.Model):
    SIZES = (
        ("small","SMALL"),
        ("medium", "MEDIUM"),
        ("large", "LARGE"),
    )

    name = models.CharField(max_length=100, verbose_name="Product Name")
    price = models.DecimalField(default=0.0, max_digits=15, decimal_places=2, verbose_name="Product Price")
    description = models.CharField(max_length=1000, verbose_name="Product Description")
    size = models.CharField(max_length=20, choices=SIZES)
    image = models.ImageField(upload_to="products/")
    weight = models.DecimalField(default=0.0, max_digits=6, decimal_places=2, verbose_name="Weight")
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)

    def __str__(self):
         return self.name
    
    class Meta:
         ordering = ["name"]