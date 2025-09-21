from rest_framework import viewsets
from .models import Product
from .serializers import ProductSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter

# Create your views here.

class ProductViewSet (viewsets.ReadOnlyModelViewSet):
  queryset = Product.objects.all()
  serializer_class = ProductSerializer
  filter_backends = [DjangoFilterBackend,SearchFilter]
  filterset_fields = ['category']
  search_fields = ['name','description']