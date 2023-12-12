from rest_framework import serializers
from .models import Project, ProjectImage, Category, SubCategory, ProjectTechnologies, PortfolioTechnologies, PortfolioCategory

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'

class ProjectImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectImage
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class SubCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = SubCategory
        fields = '__all__'

class PortfolioCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = PortfolioCategory
        exclude = ['portfolio']

class PortfolioTechnologiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = PortfolioTechnologies
        exclude = ['portfolio']

class ProjectTechnologiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectTechnologies
        fields = '__all__'
        