from rest_framework.permissions import BasePermission

class IsBuyer(BasePermission):
  def has_permission(self, request, view):
    return request.user.is_authenticated and request.user.role == 'buyer'
  
class IsSupplier(BasePermission):
  def has_permission(self, request, view):
    return request.user.is_authenticated and request.user.role == 'supplier'
  
class IsAdmin(BasePermission):
  def has_permission(self, request, view):
    return request.user.is_authenticated and request.user.roll == 'admin'
  
class IsNotAuthenticated(BasePermission):
  def has_permission(self, request, view):
    return not request.user.is_authenticated