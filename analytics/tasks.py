from celery import shared_task
from .models import SalesReport
from authentication.models import User
from orders.models import Order
from django.db import models
@shared_task
def generate_sales_report():
    for user in User.objects.filter(is_vendor=True):
        total_sales = Order.objects.filter(product__vendor=user).aggregate(total=models.Sum('product__price'))
        SalesReport.objects.create(vendor=user, total_sales=total_sales['total'])
