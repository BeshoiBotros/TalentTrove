from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from talentTrove.shortcuts import object_is_exist
from .models import Portfolio
from .serializers import PortfolioSerializer
from rest_framework.response import Response
from .models import Portfolio
from talentTrove.shortcuts import object_is_exist

class PortfolioView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk=None):
        if pk:
            instance = object_is_exist(pk=pk, model=Portfolio)
            serializer = PortfolioSerializer(instance)
            return Response(serializer.data)
        else:
            queryset = Portfolio.objects.all()
            serializer = PortfolioSerializer(queryset, many=True)
            return Response(serializer.data)

    def put(self, request):
        try:
            cv_file_type = request.FILES['cv'].content_type
        except:
            cv_file_type = None
        instance = object_is_exist(pk=Portfolio.objects.get(user_id=request.user.id).pk, model=Portfolio)
        serializer = PortfolioSerializer(instance=instance, data=request.data)
        if serializer.is_valid():
            if cv_file_type == 'application/pdf':
                serializer.save()
                return Response(serializer.data)
            elif cv_file_type == None:
                serializer.save()
                return Response(serializer.data)
            else:
                return Response({'Error' : 'cv must be pdf only'})
        else:
            return Response(serializer.errors)

    def patch(self, request):
        try:
            cv_file_type = request.FILES['cv'].content_type
        except:
            cv_file_type = None
        instance = object_is_exist(pk=Portfolio.objects.get(user_id=request.user.id).pk, model=Portfolio)
        serializer = PortfolioSerializer(instance=instance, data=request.data, partial=True)
        if serializer.is_valid():
            if cv_file_type == 'application/pdf':
                serializer.save()
                return Response(serializer.data)
            elif cv_file_type == None:
                serializer.save()
                return Response(serializer.data)
            else:
                return Response({'Error' : 'cv must be pdf only'})
        else:
            return Response(serializer.errors)