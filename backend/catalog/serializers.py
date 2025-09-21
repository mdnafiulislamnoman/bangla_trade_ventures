from rest_framework import serializers
from .models import Product, ProductImage

class ProductImageSerializer (serializers.ModelSerializer):
  class Meta:
    model = ProductImage
    fields = ['image']
  
class ProductSerializer (serializers.ModelSerializer):
  images = ProductImageSerializer(many = True, read_only = True)
  supplier_name = serializers.CharField(source = 'supplier.company_name', read_only = True)

  class Meta:
    model = Product
    fields = ['id', 'name', 'description', 'category', 'price_per_unit', 'unit', 'images', 'supplier_name']