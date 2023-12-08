from django.contrib.auth.models import User
from rest_framework.exceptions import ValidationError
from projects.models import Project
from portfolios.models import Portfolio

def object_is_exist(pk, model):
    try:
        return model.objects.get(pk=pk)
    except model.DoesNotExist:
        raise ValidationError({'Error' : 'This object not found'})

def isAuth(request):
    try:
        user = request.user
        User.objects.get(pk = user.id)
        return True
    except User.DoesNotExist:
        return False
    
def isProjectOwner(request, project_pk):
    try:
        portfolio = Portfolio.objects.get(user_id = request.user)
        project = Project.objects.get(portfolio_id=portfolio, pk=project_pk)
        return True, project
    except Portfolio.DoesNotExist:
        raise ValidationError({'Error':'This portfolio not found.'})
    except Project.DoesNotExist:
        raise ValidationError({'Error' : 'This project Does not found'})

