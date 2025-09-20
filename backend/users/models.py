from django.db import models

# Create your models here.

#This is importing Users from contrib or the user who registered in given django authentication system 
from django.contrib.auth.models import AbstractUser

#This is where im making another model for users and making sure they are imported from authenticated user.This will define user role.
class User(AbstractUser):
  Role_Choices = [
    ('buyer','Buyer'),
    ('supplier','Supplier'),
    ('admin','Admin'),
  ]
  role = models.CharField(max_length=10,choices=Role_Choices,default='buyer')

class SupplierProfile (models.Model):
  user = models.OneToOneField(User,on_delete=models.CASCADE,related_name='supplier_profile')
  company_name = models.CharField(max_length=200)
  address = models.TextField()
  phone = models.CharField(max_length=20, blank=True)
  is_verified = models.BooleanField(default=False)
  logo = models.ImageField(upload_to='suppliers/logos/', blank=True, null=True)

  def __str__(self):
    return self.company_name