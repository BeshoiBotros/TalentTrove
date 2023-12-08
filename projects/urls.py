from django.urls import path
from .views import ProjectView

urlpatterns = [
    path('', ProjectView.as_view()),
    path('<int:pk>/', ProjectView.as_view()),
]