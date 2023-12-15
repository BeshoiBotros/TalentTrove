from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from talentTrove.shortcuts import object_is_exist
from .models import Portfolio, PortfolioViewModel
from .serializers import PortfolioSerializer, PortfolioViewsSerializer
from rest_framework.response import Response
from talentTrove.shortcuts import object_is_exist
from django.utils import timezone

class PortfolioView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk=None):
        owenPortfolio = object_is_exist(pk=Portfolio.objects.get(user_id=request.user).pk, model=Portfolio)
        currentDate = timezone.now().date()
        if pk:
            instance = object_is_exist(pk=pk, model=Portfolio)
            if pk != owenPortfolio.pk:
                alreadyViewd = PortfolioViewModel.objects.filter(user=request.user, date__date=currentDate, portfolio=instance).first()
                if not alreadyViewd:
                    PortfolioViewModel.objects.create(user = request.user, portfolio=instance)
            serializer = PortfolioSerializer(instance)
            return Response(serializer.data)
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

class PortfolioViews(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, portfolio_pk):
        portfolio = object_is_exist(portfolio_pk, Portfolio)
        portfolio_views = PortfolioViewModel.objects.filter(portfolio_id=portfolio)
        portfolio_views_not_repeted = []
        portfolio_views_users = []
        for view in portfolio_views:
            if view.user.pk not in portfolio_views_users:
                portfolio_views_not_repeted.append(view)
                portfolio_views_users.append(view.user.pk)
        portfolio_views_not_repeted_serializer = PortfolioViewsSerializer(portfolio_views, many=True)
        data = portfolio_views_not_repeted_serializer.data
        data += [{'views': len(portfolio_views_not_repeted)}]
        return Response(data)