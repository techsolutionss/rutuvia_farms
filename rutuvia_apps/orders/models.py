from django.db import models

# Create your models here.
class Order(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    order_id = models.CharField(max_length=100, unique=True)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_status = models.CharField(max_length=20, default='PENDING')
    created_at = models.DateTimeField(auto_now_add=True)
    email_sent = models.BooleanField(default=False, verbose_name="Confirmation Email Sent",)

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ["user"]