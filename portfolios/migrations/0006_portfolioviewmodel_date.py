# Generated by Django 5.0 on 2023-12-14 15:16

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolios', '0005_rename_portfolioview_portfolioviewmodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='portfolioviewmodel',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]