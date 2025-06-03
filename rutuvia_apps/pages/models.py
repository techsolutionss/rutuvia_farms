from django.db import models

class Contact(models.Model):
    fullname = models.CharField(max_length=100, verbose_name="Full Name")
    email = models.EmailField(max_length=50, verbose_name="Email Address")
    phone = models.CharField(max_length=15, verbose_name="Phone Number")
    subject = models.CharField(max_length=100, verbose_name="Subject")
    message = models.TextField(verbose_name="Message")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created At")

    def __str__(self):
        return f"{self.fullname} - {self.subject}"
    
    class Meta:
        verbose_name = "Contact"
        verbose_name_plural = "Contact"
        ordering = ["-created_at"]

class Service(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to="services/")

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Service"
        verbose_name_plural = "Services"