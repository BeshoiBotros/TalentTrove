# Generated by Django 5.0 on 2023-12-13 18:56

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0006_projectview'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ProjectView',
            new_name='ProjectViewModel',
        ),
    ]
