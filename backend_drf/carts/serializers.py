from rest_framework import serializers
from .models import Cart, CartItem


class CartItemSerializer(serializers.ModelSerializer):
    # fetching from product model
    product_name = serializers.CharField(source='product.name', read_only=True)
    price = serializers.DecimalField(source='product.price', max_digits=10, decimal_places=2, read_only=True)
    tax_percent = serializers.DecimalField(source='product.tax_percent',max_digits=10, decimal_places=2, read_only=True)
    class Meta:
        model = CartItem
        fields = "__all__"

# using nested serializer as items. many = True means cart can have many cart items
class CartSerializer(serializers.ModelSerializer):
    items = CartItemSerializer(many=True)
    # use this method to call get subtotal func
    subtotal = serializers.DecimalField(max_digits=10, decimal_places=2)
    grand_total = serializers.DecimalField(max_digits=10, decimal_places=2)
    class Meta:
        model = Cart
        fields = "__all__"
    

