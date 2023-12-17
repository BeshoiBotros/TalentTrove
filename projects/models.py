from django.db import models
from portfolios.models import Portfolio
from django.contrib.auth.models import User
from django.utils import timezone
from django.db.models.signals import post_save
from django.dispatch import receiver

class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)

class Project(models.Model):
    general_image = models.ImageField(upload_to='projects/generalImages/')
    link = models.URLField(null=True, blank=True)
    discription = models.TextField(null=False, blank=False)
    title = models.CharField(max_length=255, null=False, blank=False)
    portfolio_id = models.ForeignKey(Portfolio, on_delete=models.CASCADE)
    project_category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    def __str__(self) -> str:
        return self.title

class ProjectImage(models.Model):
    project_id = models.ForeignKey(Project, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='project-images/')


class SubCategory(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)

class ProjectTechnologies(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    sub_category = models.ForeignKey(SubCategory, on_delete=models.CASCADE)

class PortfolioCategory(models.Model):
    portfolio = models.OneToOneField(Portfolio, on_delete=models.CASCADE)
    category = models.ManyToManyField(Category, blank=True, null=True)

class PortfolioTechnologies(models.Model):
    portfolio = models.OneToOneField(Portfolio, on_delete=models.CASCADE)
    sub_category = models.ManyToManyField(SubCategory, blank=True)

class ProjectViewModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    date = models.DateTimeField(default=timezone.now)

    def __str__(self) -> str:
        return f'{self.user.username} has view {self.project.portfolio_id.user_id.username} project : {self.project.title}'


@receiver(post_save, sender=Portfolio)
def create_portfolioNeeds(sender, created, instance, **kwargs):
    if created:
        PortfolioTechnologies.objects.create(portfolio=instance)
        PortfolioCategory.objects.create(portfolio=instance)

