from django.urls import path
from .views import ProductListCreateView, CategoryListCreateView
from .views import product_list, product_detail, add_product
urlpatterns = [
    path('products/', ProductListCreateView.as_view(), name='product-list-create'),
    path('categories/', CategoryListCreateView.as_view(), name='category-list-create'),
    path('', product_list, name='product_list'),
    path('<int:pk>/', product_detail, name='product_detail'),
    path('add/', add_product, name='add_product'),


]
