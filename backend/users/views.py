from rest_framework import generics, permissions
from rest_framework_simplejwt.views import TokenObtainPairView
from .models import User
from .serializers import UserSerializer
from .permissions import IsNotAuthenticated

# Create your views here.
class RegisterView (generics.CreateAPIView):
  queryset = User.objects.all()
  serializer_class = UserSerializer
  permission_classes = [IsNotAuthenticated]

class LoginView (TokenObtainPairView):
  permission_classes = [IsNotAuthenticated]