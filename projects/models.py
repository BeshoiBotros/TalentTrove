from django.db import models
from portfolios.models import Portfolio
from django.contrib.auth.models import User
from django.utils import timezone

class Project(models.Model):
    general_image = models.ImageField(upload_to='projects/generalImages/')
    link = models.URLField(null=True, blank=True)
    discription = models.TextField(null=False, blank=False)
    title = models.CharField(max_length=255, null=False, blank=False)
    portfolio_id = models.ForeignKey(Portfolio, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.title

class ProjectImage(models.Model):
    project_id = models.ForeignKey(Project, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='project-images/')

class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)

class SubCategory(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)

class ProjectTechnologies(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    sub_category = models.ForeignKey(SubCategory, on_delete=models.CASCADE)

class PortfolioCategory(models.Model):
    portfolio = models.ForeignKey(Portfolio, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

class PortfolioTechnologies(models.Model):
    portfolio = models.ForeignKey(Portfolio, on_delete=models.CASCADE)
    sub_category = models.ForeignKey(SubCategory, on_delete=models.CASCADE)

class ProjectViewModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    date = models.DateTimeField(default=timezone.now)

    def __str__(self) -> str:
        return f'{self.user.username} has view {self.project.portfolio_id.user_id.username} project : {self.project.title}'

