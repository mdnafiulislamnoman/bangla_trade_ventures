from rest_framework import serializers
from .models import RFQ
from users.models import User

class RFQSerializer (serializers.ModelSerializer):
  buyer_name = serializers.CharField(source = 'buyer.username',read_only = True)
  product_name = serializers.CharField(source = 'product.name',read_only = True)

  class Meta:
    model = RFQ
    fields = ['id', 'buyer_name', 'product_name', 'quantity', 'message', 'delivery_date', 'status', 'created_at']
    read_only_fields = ['id','buyer_name', 'product_name', 'created_at']