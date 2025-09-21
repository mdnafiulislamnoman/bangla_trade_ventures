from rest_framework import generics, permissions
from .models import RFQ
from .serializers import RFQSerializer
from users.permissions import IsBuyer

# Create your views here.

class RFQCreateView (generics.CreateAPIView):
  queryset = RFQ.objects.all()
  serializer_class = RFQSerializer
  permission_classes = [IsBuyer]

  def perform_create(self, serializer):
    serializer.save(buyer = self.request.user)