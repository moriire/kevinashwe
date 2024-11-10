from django.db import models
from books.models import BooksModel

class Order(models.Model):
    created_by =  models.CharField(max_length=50)
    email = models.EmailField()
    cart = models.ForeignKey(BooksModel, related_name="order_cart", on_delete=models.CASCADE)
    #authorization_code = models.CharField(max_length=16, blank=True, null=True)
    reference_code = models.CharField(max_length=12, blank=True, null=True)
    amount = models.FloatField()
    #status = models.CharField(max_length=9, choices=OrderStatus.choices, default="UNPAID")
    #address = models.TextField(default="")
    #city = models.CharField(max_length=80, null=True, blank=True)
    created_on = models.DateTimeField(auto_now=True)
    
    def __str__(self) -> str:
        return self.cart.title