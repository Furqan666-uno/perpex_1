from django.urls import path
from .views import UserRegistrationView, OrderView, PaymentView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('login/', TokenObtainPairView.as_view(), name='login'),
    path('token/refresh/', TokenRefreshView.as_view(), name='refresh'),
    path('payments/', PaymentView.as_view(), name='payments'),
    path('orders/', OrderView.as_view(), name='orders'),
]
