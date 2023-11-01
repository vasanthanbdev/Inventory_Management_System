from rest_framework import serializers
from .models import *

#products
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['name', 'description', 'category', 'price', 'quantity', 'preferred_vendor', 'reorder_level']
        
#warehouses
class WarehouseSeializer(serializers.ModelSerializer):
    class Meta:
        model = Warehouse
        fields = ['name', 'email', 'contact', 'city', 'address']


#vendors
class VendorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendor
        fields = ['name', 'email', 'contact', 'city', 'address']
        

#customers
class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['name', 'email', 'contact', 'city', 'address']
        

#purchase orders
class PurchaseOrderItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = PurchaseOrderItem
        fields = ['item', 'quantity', 'total_item_price']

class PurchaseOrderSerializer(serializers.ModelSerializer):
    items = PurchaseOrderItemSerializer(many=True)
    
    class Meta:
        model = PurchaseOrder
        fields = ['order_date', 'delivery_date', 'vendor', 'warehouse', 'items']
        
    def create(self, validated_data):
        items_data = validated_data.pop('items')
        purchase_order = PurchaseOrder.objects.create(**validated_data)
        
        for item in items_data:
            PurchaseOrderItem.objects.create(purchase_order=purchase_order, **item)
            
        return purchase_order