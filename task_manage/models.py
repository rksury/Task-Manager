from django.db import models
from user.models import User


class Project(models.Model):
    project_name = models.CharField(max_length=200, unique=True)

class Task(models.Model):
    task_name = models.CharField(max_length=100, unique=True)
    task_description = models.CharField(max_length=200, blank=True, default='')
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    project = models.ForeignKey(Project, null=False, on_delete=models.CASCADE)
    status = models.BooleanField(default=False)
