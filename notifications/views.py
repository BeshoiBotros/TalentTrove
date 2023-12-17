from django.shortcuts import render
from rest_framework.views import APIView
from .models import LikeNotification
from talentTrove.shortcuts import object_is_exist
from .serializers import NotificationSerializer
from rest_framework.response import Response

class NotificationView(APIView):
    def get(self, request, pk=None):
        pass
