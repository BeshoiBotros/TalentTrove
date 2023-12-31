# Generated by Django 5.0 on 2023-12-17 13:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolios', '0006_portfolioviewmodel_date'),
        ('projects', '0009_alter_portfoliocategory_portfolio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portfoliocategory',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='projects.category'),
        ),
        migrations.AlterField(
            model_name='portfoliotechnologies',
            name='portfolio',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='portfolios.portfolio'),
        ),
        migrations.RemoveField(
            model_name='portfoliotechnologies',
            name='sub_category',
        ),
        migrations.AddField(
            model_name='portfoliotechnologies',
            name='sub_category',
            field=models.ManyToManyField(blank=True, to='projects.subcategory'),
        ),
    ]
