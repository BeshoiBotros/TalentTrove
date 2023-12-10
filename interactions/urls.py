from django.urls import path
from .views import LikeView, CommentView
urlpatterns = [
    # -Like URLS 
    path('like/', LikeView.as_view()),
    path('like/<int:pk>/', LikeView.as_view()),
    path('like/<int:project_pk>/', LikeView.as_view())
]