from django.db import models
from authentication.models import User

class SalesReport(models.Model):
    vendor = models.ForeignKey(User, on_delete=models.CASCADE)
    total_sales = models.DecimalField(max_digits=10, decimal_places=2)
    report_date = models.DateField(auto_now_add=True)
