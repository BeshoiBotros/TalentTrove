from rest_framework import serializers
from .models import Portfolio, PortfolioViewModel

class PortfolioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Portfolio
        exclude = ['user_id']

class PortfolioViewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = PortfolioViewModel
        fields = '__all__'