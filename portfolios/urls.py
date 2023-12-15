from django.urls import path
from .views import PortfolioView, PortfolioViews

urlpatterns = [
    
    path('', PortfolioView.as_view()),
    path('<int:pk>/', PortfolioView.as_view()),

    path('views/portfolio/<int:portfolio_pk>/', PortfolioViews.as_view()),
]