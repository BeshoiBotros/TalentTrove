from django.urls import path
from .views import PortfolioView
urlpatterns = [
    path('', PortfolioView.as_view()),
    path('<int:pk>/', PortfolioView.as_view())
]