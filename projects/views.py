from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from .models import Project, ProjectImage
from .serializer import ProjectSerializer, ProjectImageSerializer
from rest_framework.response import Response
from talentTrove.shortcuts import object_is_exist, isProjectOwner
from portfolios.models import Portfolio

class ProjectView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk=None):
        if pk:
            instance = object_is_exist(pk=pk, model=Project)
            serializer = ProjectSerializer(instance=instance)
            return Response(serializer.data)
        queryset = Project.objects.all()
        serializer = ProjectSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request):
        portfolio = object_is_exist(pk=Portfolio.objects.get(user_id=request.user).pk, model=Portfolio)
        request.data['portfolio_id'] = portfolio.pk
        serializer = ProjectSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def put(self, request, pk):
        isOwner, project = isProjectOwner(request=request, project_pk=pk)
        if isOwner:
            mutable_data = request.data.copy()
            mutable_data['portfolio_id'] = project.portfolio_id.pk
            serializer = ProjectSerializer(instance=project, data=request.data)
            if serializer.is_valid():
                return Response(serializer.data)
            else:
                return Response(serializer.errors)
        else:
            return Response({'Error' : 'This project does not belong to you.'})

    def patch(self, request, pk):
        isOwner, project = isProjectOwner(request=request, project_pk=pk)
        if isOwner:
            mutable_data = request.data.copy()
            mutable_data['portfolio_id'] = project.portfolio_id.pk
            serializer = ProjectSerializer(instance=project, data=request.data, partial=True)
            if serializer.is_valid():
                return Response(serializer.data)
            else:
                return Response(serializer.errors)
        else:
            return Response({'Error' : 'This project does not belong to you.'})

    def delete(self, request, pk):
        isOwner, project = isProjectOwner(request=request, project_pk=pk)
        if isOwner:
            project.delete()
            return Response({'message' : 'project has been deleted successfuly'})
        return Response({'Error' : 'This project does not belong to you.'})
