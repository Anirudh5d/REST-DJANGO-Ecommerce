from django.db import models
from authentication.models import User
from products.models import Product

class Order(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    status = models.CharField(max_length=255, default='Pending')
    created_at = models.DateTimeField(auto_now_add=True)
