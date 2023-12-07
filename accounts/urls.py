from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from django.urls import path
from .views import UserView
urlpatterns = [
    
    path('accounts/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('accounts/', UserView.as_view()),
    path('accounts/<int:pk>/', UserView.as_view()),
]