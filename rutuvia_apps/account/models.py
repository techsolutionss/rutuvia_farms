from django.db import models

class Account(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    phone = models.CharField(max_length=50)
    password = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.firstname}-{self.lastname}"
    
    class Meta:
        ordering = ["-created_at"]