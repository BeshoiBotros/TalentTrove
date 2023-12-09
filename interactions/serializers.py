from rest_framework import serializers
from .models import Comment, Like

class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        exclude = ['user_id']

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        exclude = ['user_id']