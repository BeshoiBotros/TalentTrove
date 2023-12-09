from django.db import models
from portfolios.models import Portfolio


class Project(models.Model):
    general_image = models.ImageField(upload_to='projects/generalImages/')
    link = models.URLField(null=True, blank=True)
    discription = models.TextField(null=False, blank=False)
    title = models.CharField(max_length=255, null=False, blank=False)
    portfolio_id = models.ForeignKey(Portfolio, on_delete=models.CASCADE)


class ProjectImage(models.Model):
    project_id = models.ForeignKey(Project, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='project-images/')