from django.contrib import admin
from .models import ProjectViewModel, Project

admin.site.register(ProjectViewModel)
admin.site.register(Project)