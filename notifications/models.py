from django.db import models
from interactions.models import Like
from django.db.models.signals import post_save
from django.dispatch import receiver

class LikeNotification(models.Model):
    like = models.ForeignKey(Like, on_delete=models.CASCADE)
    message = models.TextField(null=False, blank=False)

@receiver(post_save, sender=Like)
def create_notification(sender, created, instance, **kwargs):
    if created:
        LikeNotification.objects.create(like = instance, message=f'User {instance.user_id.username} liked on your project')