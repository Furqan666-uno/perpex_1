from django.urls import path, include
from django.conf import settings
import debug_toolbar
from .views import UserRegistrationView, OrderView, PaymentView, MenuItemView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('login/', TokenObtainPairView.as_view(), name='login'),
    path('token/refresh/', TokenRefreshView.as_view(), name='refresh'),
    path('payments/', PaymentView.as_view(), name='payments'),
    path('orders/', OrderView.as_view(), name='orders'),
    path('menu/', MenuItemView.as_view(), name='menu'),
]

if settings.DEBUG:
    urlpatterns += [
        path('__debug__', include(debug_toolbar.urls))
    ]
