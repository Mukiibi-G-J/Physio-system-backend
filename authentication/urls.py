from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from .views import *
from django.urls import path

app_name = 'authentication'

urlpatterns = [
    path('register/', CreateUserView.as_view(), name='register'),
    path('check_username/', CheckUsername.as_view(), name='check_username'),
    path('check_email/', CheckEmail.as_view(), name='check_email'),
    path('verification/', VerifyEmail.as_view(), name='verify_email'),
    path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
 
]