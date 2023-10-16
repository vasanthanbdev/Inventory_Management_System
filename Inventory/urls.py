from django.urls import path
from .views import *


urlpatterns = [
    path('products/', ProductList.as_view(), name='product_list'),
    path('products/<int:pk>/', ProductDetail.as_view(), name='product_detail'),
    
    path('vendors/', VendorList.as_view(), name='vendor_list'),
    path('vendors/<int:pk>/', VendorDetail.as_view(), name='vendor_detail'),
    
    path('warehouses/', WarehouseList.as_view(), name='warehouse_list'),
    path('warehouses/<int:pk>/', WarehouseDetail.as_view(), name='warehouse_detail'),
    
    path('customers/', CustomerList.as_view(), name='customer_list'),
    path('customers/<int:pk>/', CustomerDetail.as_view(), name='customer_detail'),
]