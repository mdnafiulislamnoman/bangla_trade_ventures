from django.db import models

# Create your models here.
from users.models import SupplierProfile

class Product (models.Model):
  supplier = models.ForeignKey(SupplierProfile, on_delete = models.CASCADE, related_name = 'products')
  name = models.CharField(max_length = 200)
  description = models.TextField()
  category = models.CharField(max_length=100)
  price_per_unit = models.DecimalField(max_digits = 10, decimal_places = 2)
  unit = models.CharField(max_length=50)
  created_at = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return self.name
  
class ProductImage (models.Model):
  product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')
  image = models.ImageField(upload_to = 'products/images')

  def __str__(self):
    return f"image for {self.product.name}"