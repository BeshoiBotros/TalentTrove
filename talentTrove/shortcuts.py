from django.contrib.auth.models import User
from rest_framework.exceptions import ValidationError

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
    