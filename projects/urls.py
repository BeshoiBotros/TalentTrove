from django.urls import path
from .views import ProjectView, ProjectImageView, CategoryView, SubCategoryView, PortfolioCategoryView, ProjectViews

urlpatterns = [
    path('', ProjectView.as_view()),
    path('<int:pk>/', ProjectView.as_view()),

    path('project-images/', ProjectImageView.as_view()),
    path('project-images/<int:pk>/', ProjectImageView.as_view()), # for return project image by PK or update or delete
    path('project-images/project/<int:project_pk>/', ProjectImageView.as_view()), # for return project images by project_ID

    path('category/', CategoryView.as_view()),
    path('category/<int:pk>/', CategoryView.as_view()),

    path('sub-category/', SubCategoryView.as_view()),
    path('sub-category/<int:pk>/', SubCategoryView.as_view()),
    path('sub-category/category/<int:category_pk>/', SubCategoryView.as_view()),

    path('portfolio-category/', PortfolioCategoryView.as_view()),
    path('portfolio-category/<int:pk>/', PortfolioCategoryView.as_view()),
    path('portfolio-category/portfolio/<int:portfolio_pk>/', PortfolioCategoryView.as_view()),

    path('views/project/<int:project_pk>/', ProjectViews.as_view())
    
] 