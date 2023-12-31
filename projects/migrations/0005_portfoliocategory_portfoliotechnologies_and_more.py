# Generated by Django 5.0 on 2023-12-12 14:12

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolios', '0003_alter_portfolio_cv_alter_portfolio_image'),
        ('projects', '0004_alter_category_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='PortfolioCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.category')),
                ('portfolio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portfolios.portfolio')),
            ],
        ),
        migrations.CreateModel(
            name='PortfolioTechnologies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('portfolio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portfolios.portfolio')),
                ('sub_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.subcategory')),
            ],
        ),
        migrations.CreateModel(
            name='ProjectTechnologies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.project')),
                ('sub_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.subcategory')),
            ],
        ),
    ]
