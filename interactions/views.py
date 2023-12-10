from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from .models import Like, Comment
from talentTrove.shortcuts import object_is_exist, getObjectFromReq
from .serializers import CommentSerializer, LikeSerializer
from rest_framework.response import Response
from projects.models import Project

class LikeView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk=None, project_pk=None):
        if pk:
            like = object_is_exist(pk=pk, model=Like)
            serializer = LikeSerializer(like)
            return Response(serializer.data)
        if project_pk:
            user_like_it = False
            user = request.user
            project = object_is_exist(pk=project_pk, model=Project)
            like = Like.objects.filter(project_id=project, user_id=user).first()
            if not like:
                queryset = Like.objects.filter(project_id=project)
                serializer = LikeSerializer(queryset, many=True)
                data = serializer.data.copy()
                data += [{'user_like_it': None}]
                return Response(data)
            if like.like_it:
                user_like_it = True
            queryset = Like.objects.filter(project_id=project)
            serializer = LikeSerializer(queryset, many=True)
            data = serializer.data.copy()
            data += [{'user_like_it': user_like_it}]
            return Response(data)
        queryset = Like.objects.all()
        serializer = LikeSerializer(queryset, many=True)
        return Response(serializer.data)
    

    def post(self, request):
        user = request.user
        project = getObjectFromReq(request=request, req_key='project_id', model=Project)
        like = Like.objects.filter(project_id=project, user_id=user).first()
        if not like:
            data = {'like_it' : True, 'user_id' : user.pk, 'project_id' : project.pk}
            serialzer = LikeSerializer(data=data)
            if serialzer.is_valid():
                serialzer.save()
                return Response(serialzer.data)
            else:
                return Response(serialzer.errors)
        else:
            return Response({'Error' : 'object already exist, you need to update it'})

    def put(self, request):
        user = request.user
        project = getObjectFromReq(request=request, req_key='project_id', model=Project)
        like = Like.objects.filter(project_id=project, user_id=user).first()
        if like:
            if like.like_it:
                like.like_it = False
            else:
                like.like_it = True
            data = {'like_it' : like.like_it, 'user_id' : user.pk, 'project_id' : project.pk}
            serialzer = LikeSerializer(instance=like,data=data)
            if serialzer.is_valid():
                serialzer.save()
                return Response(serialzer.data)
            else:
                return Response(serialzer.errors)
        else:
            return Response({'Error' : "object doesn't exist"})
    

class CommentView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk=None, project_pk=None):
        pass

    def post(self, request):
        pass

    def put(self, request, pk, project_pk):
        pass
    
    def patch(self, request, pk, project_pk):
        pass

    def delete(self, request, pk, project_pk):
        pass
