from .models import Category, Product, Cart, Order
from rest_framework import serializers

class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name')

class ProductListSerializer(serializers.HyperlinkedModelSerializer):
    category = serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model = Product
        fields = ('id', 'name', 'category', 'price')

class ProductDetailSerializer(serializers.HyperlinkedModelSerializer):
    category = serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model = Product
        fields = ('id', 'name', 'category', 'description', 'price')

class CartListSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model = Cart
        fields = ('id', 'user')

class CartSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True)
    products = ProductListSerializer(read_only=True, many=True)
    class Meta:
        model = Cart
        fields = ('id', 'user', 'products')
