from django.db import models
from django.contrib.auth.models import User
from projects.models import Project

class Like(models.Model):
    like_it    = models.BooleanField(default=False)
    user_id    = models.ForeignKey(User, on_delete=models.CASCADE)
    project_id = models.ForeignKey(Project, on_delete=models.CASCADE)

class Comment(models.Model):
    content = models.TextField(blank=False, null=False)
    user_id    = models.ForeignKey(User, on_delete=models.CASCADE)
    project_id = models.ForeignKey(Project, on_delete=models.CASCADE)