from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from .models import Project, ProjectImage
from .serializer import ProjectSerializer, ProjectImageSerializer, CategorySerializer, SubCategorySerializer
from rest_framework.response import Response
from talentTrove.shortcuts import object_is_exist, isProjectOwner, check_permission
from portfolios.models import Portfolio
from .models import Category, SubCategory

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
    
class ProjectImageView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk=None, project_pk=None):
        if pk:
            instance = object_is_exist(pk=pk, model=ProjectImage)
            serializer = ProjectImageSerializer(instance)
            return Response(serializer.data)
        if project_pk:
            project = object_is_exist(pk=project_pk, model=Project)
            queryset = ProjectImage.objects.filter(project_id=project)
            serializer = ProjectImageSerializer(queryset, many=True)
            return Response(serializer.data)
        queryset = ProjectImage.objects.all()
        serializer = ProjectImageSerializer(queryset, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serialzer = ProjectImageSerializer(data=request.data)
        if serialzer.is_valid():
            isOwner, project = isProjectOwner(request=request, project_pk=request.data['project_id'])
            if isOwner:
                serialzer.save()
                return Response(serialzer.data)
        return Response(serialzer.errors)
        
    
    def put(self, request, pk):
        instance = object_is_exist(pk=pk, model=ProjectImage)
        isOwner, project = isProjectOwner(request=request, project_pk=instance.project_id.pk)
        if isOwner:
            serialzer = ProjectImageSerializer(instance=instance, data=request.data)
            if serialzer.is_valid():
                serialzer.save()
                return Response(serialzer.data)
            return Response(serialzer.errors)

    def patch(self, request, pk):
        instance = object_is_exist(pk=pk, model=ProjectImage)
        isOwner, project = isProjectOwner(request=request, project_pk=instance.project_id.pk)
        if isOwner:
            serialzer = ProjectImageSerializer(instance=instance, data=request.data, partial=True)
            if serialzer.is_valid():
                serialzer.save()
                return Response(serialzer.data)
            return Response(serialzer.errors)

    def delete(self, request, pk):
        instance = object_is_exist(pk=pk, model=ProjectImage)
        isOwner, project = isProjectOwner(request=request, project_pk=instance.project_id.pk)
        if isOwner:
            instance.delete()
            instance.save()
            return Response({'Message' : 'object has been deleted successfully'})

class CategoryView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk=None):
        if pk:
            category = object_is_exist(pk=pk, model=Category)
            serializer = CategorySerializer(category)
            return Response(serializer.data)
        queryset = Category.objects.all()
        serializer = CategorySerializer(queryset, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        can_add_category = check_permission(permission_name='add_category', request=request)
        if can_add_category:
            serializer = CategorySerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            else:
                return Response(serializer.errors)
        else:
            return Response({'Message' : 'you can not perform this action'})
        

    def patch(self, request, pk):
       can_update_category = check_permission(permission_name="change_category", request=request)
       if can_update_category :
           instance = object_is_exist(pk=pk, model=Category)
           serializer = CategorySerializer(instance=instance, data=request.data, partial=True)
           if serializer.is_valid():
               serializer.save()
               return Response(serializer.data)
           else:
               return Response(serializer.errors)
       else:
           return Response({'Message' : 'you can not perform this actoin'})

    def delete(self, request, pk):
        can_delete_category = check_permission(permission_name='delete_category', request=request)
        if can_delete_category:
            category = object_is_exist(pk=pk, model=Category)
            category.delete()
            return Response({'message':'the category has been deleted successfully'})

class SubCategoryView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk=None, category_pk=None):
        if pk:
            sub_category = object_is_exist(pk=pk, model=SubCategory)
            serializer = SubCategorySerializer(sub_category)
            return Response(serializer.data)
        if category_pk:
            category = object_is_exist(pk=category_pk, model=Category)
            queryset = SubCategory.objects.filter(category=category)
            serializer = SubCategorySerializer(queryset, many=True)
        queryset = SubCategory.objects.all()
        serializer = SubCategorySerializer(queryset, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        can_add_sub_category = check_permission(permission_name='add_subcategory', request=request)
        if can_add_sub_category:
            serializer = SubCategorySerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            else:
                return Response(serializer.errors)
        else:
            return Response({'Message' : 'you can not perform this action'})