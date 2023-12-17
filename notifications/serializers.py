from rest_framework import serializers
from .models import LikeNotification

class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = LikeNotification
        fields = '__all__'