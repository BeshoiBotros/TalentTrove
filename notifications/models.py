from django.db import models
from django.contrib.auth.models import User

class Notification(models.Model):
    to_user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField(null=False, blank=False)
