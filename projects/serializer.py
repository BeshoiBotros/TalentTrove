from rest_framework import serializers
from .models import Project, ProjectImage, Category, SubCategory

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