# Generated by Django 5.0 on 2023-12-08 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolios', '0002_alter_portfolio_user_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portfolio',
            name='cv',
            field=models.FileField(blank=True, default='portfolios/CVs/defCV.pdf', null=True, upload_to='portfolios/CVs/'),
        ),
        migrations.AlterField(
            model_name='portfolio',
            name='image',
            field=models.ImageField(blank=True, default='portfolios/images/def.jpg', null=True, upload_to='portfolios/images/'),
        ),
    ]
