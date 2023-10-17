from django.urls import path, include
from .views import *
from rest_framework.routers import DefaultRouter 

router = DefaultRouter()
router.register(r'products', Product)
router.register(r'vendors', Vendor)
router.register(r'customers', Customer)
router.register(r'warehouses', Warehouse)
router.register(r'purchaseorders', PurchaseOrderViewSet)

urlpatterns = [
    path('', include(router.urls))
]