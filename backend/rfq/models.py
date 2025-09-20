from django.db import models

# Create your models here.
from users.models import User
from catalog.models import Product

class RFQ (models.Model):
  buyer = models.ForeignKey(User, on_delete = models.CASCADE, related_name = 'rfqs_made')
  product = models.ForeignKey(Product, on_delete = models.CASCADE)
  quantity = models.PositiveIntegerField()
  message = models.TextField(blank = True)
  delivery_date = models.DateField()
  status = models.CharField(max_length = 20, default = 'pending')
  created_at = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return f"RFQ #{self.id} from {self.buyer.username}"