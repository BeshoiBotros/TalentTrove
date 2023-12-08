from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Portfolio(models.Model):
    user_id = models.OneToOneField(User, on_delete=models.CASCADE)
    title_job = models.CharField(max_length=255, default='Null', null=True, blank=True)
    discription = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='portfolios/images/', null=True, blank=True, default='portfolios/images/def.jpg')
    cv = models.FileField(upload_to='portfolios/CVs/', null=True, blank=True, default='portfolios/CVs/defCV.pdf')
    github_link = models.URLField(null=True, blank=True)
    linkedin_link = models.URLField(null=True, blank=True)
    phone_no = models.CharField(max_length=15, null=True, blank=True)

    def __str__(self) -> str:
        return self.user_id.username + ' Portfolio'


@receiver(post_save, sender=User)
def create_portfilio(sender, created, instance, **kwargs):
    if created:
        Portfolio.objects.create(user_id = instance)