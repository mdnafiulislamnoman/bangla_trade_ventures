from django.urls import path, include
from rest_framework.routers import DefaultRouter
from catalog.views import ProductViewSet
from rfq.views import RFQCreateView
from users.views import RegisterView, LoginView
from rest_framework_simplejwt.views import TokenRefreshView

router = DefaultRouter
router.register(r'products',ProductViewSet)

urlpatterns = [
    path('',include(router.urls)),
    path('auth/register', RegisterView.as_view(),name='register'),
    path('auth/login', LoginView.as_view(),name='login'),
    path('auth/token/refresh', TokenRefreshView.as_view(),name='token_refresh'),
    path('rfqs/', RFQCreateView.as_view(),name='rfq-create'),
]
