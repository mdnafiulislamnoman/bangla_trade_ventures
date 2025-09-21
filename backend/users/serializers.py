from rest_framework import serializers
from .models import User, SupplierProfile

class UserSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = ['id', 'username', 'email', 'role']

class SupplierProfileSerializer (serializers.ModelSerializer):
  user = UserSerializer(read_only = True)

  class Meta:
    model = SupplierProfile
    fields = ['id', 'user', 'company_name', 'address', 'phone', 'is_verified', 'logo']