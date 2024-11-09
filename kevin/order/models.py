from django.db import models
from product.models import Product
from thumbs.models import ProductImage

class Order(models.Model):
    class OrderStatus(models.TextChoices):
        UNPAID = "unpaid"
        PAID = "paid"
        DELIVERED = "delivered"
        COMPLETED = "completed"

    created_by =  models.CharField(max_length=50)
    created_for =  models.CharField(max_length=50)
    for_email = models.EmailField()
    by_email = models.EmailField()
    cart = models.ManyToManyField(Product, blank=True)
    authorization_code = models.CharField(max_length=16, blank=True, null=True)
    reference_code = models.CharField(max_length=12, blank=True, null=True)
    amount = models.FloatField()
    status = models.CharField(max_length=9, choices=OrderStatus.choices, default="UNPAID")
    address = models.TextField(default="")
    city = models.CharField(max_length=80, null=True, blank=True)
    mode = models.CharField(max_length=10, choices=(("ship", "ship"), ("pickup", "pickup")))
    created_on = models.DateTimeField(auto_now=True)
    
    def __str__(self) -> str:
        return self.status