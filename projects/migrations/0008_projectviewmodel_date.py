# Generated by Django 5.0 on 2023-12-14 16:51

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0007_rename_projectview_projectviewmodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='projectviewmodel',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
