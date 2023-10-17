from django.urls import path, include
from .views import *
from rest_framework.routers import DefaultRouter 

router = DefaultRouter()
router.register(r'products', ProductViewSet, basename='products')
router.register(r'vendors', VendorViewSet, basename='vendors')
router.register(r'customers', CustomerViewSet, basename='customers')
router.register(r'warehouses', WarehouseViewSet, basename='warehouses')
router.register(r'purchaseorders', PurchaseOrderViewSet, basename='purchaseorders')

urlpatterns = [
    path('', include(router.urls))
]