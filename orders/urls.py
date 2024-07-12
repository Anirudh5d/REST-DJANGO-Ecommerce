from django.urls import path
from .views import OrderListCreateView
from .views import order_list, order_detail, create_order

urlpatterns = [
    path('orders/', OrderListCreateView.as_view(), name='order-list-create'),
    path('', order_list, name='order_list'),
    path('<int:pk>/', order_detail, name='order_detail'),
    path('create/', create_order, name='create_order'),
]
