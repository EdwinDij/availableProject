from rest_framework import serializers
from .models import Product, Shop, Customer

class ShopSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shop
        fields = ('shop_name', 'email', 'password')
        
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
        
class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'
        