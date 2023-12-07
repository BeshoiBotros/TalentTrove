from django.shortcuts import render
from rest_framework.views import APIView
from django.contrib.auth.models import User
from rest_framework.response import Response
from talentTrove.shortcuts import object_is_exist, isAuth
from .serializer import UserSerializer, UserSerializerForUpdate
from rest_framework import status

class UserView(APIView):
    def get(self, request, pk=None):
        auth = isAuth(request=request)
        if auth:
            if pk:
                instance = object_is_exist(pk=pk, model=User)
                serializer = UserSerializer(instance)
                return Response(serializer)
            else:
                queryset = User.objects.all()
                serializer = UserSerializer(queryset, many=True)
                return Response(serializer.data)
        else:
            return Response({'message' : 'you may have to login'}, status=status.HTTP_401_UNAUTHORIZED)
        

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


    def put(self, request):
        auth = isAuth(request=request)
        if auth:
            instance = object_is_exist(pk=request.user.id, model=User)
            serializer = UserSerializerForUpdate(instance, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            else:
                return Response(serializer.errors)
        else:
            return Response({'message' : 'you may have to login'})
    
    def patch(self, request):
        auth = isAuth(request=request)
        if auth:
            instance = object_is_exist(pk=request.user.id, model=User)
            serializer = UserSerializerForUpdate(instance, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            else:
                return Response(serializer.errors)
        else:
            return Response({'message' : 'you may have to login'})

    def delete(self, request):
        auth = isAuth(request=request)
        if auth:
            instance = object_is_exist(pk=request.user.id, model=User)
            instance.is_active = False
            instance.save()
        else:
            return Response({'message' : 'you may have to login'})
        