from django.db import models
from user.models import User

class TaskEntry(models.Model):
    class Meta:
        db_table = 'task_manage__TaskEntry'

    task_description = models.CharField(max_length=200, default='No Description')
    user = models.ForeignKey(User, null=False, on_delete=models.CASCADE)
    start_time = models.DateTimeField(null=False, blank=False)
    end_time = models.DateTimeField(null=False, blank=False)
    LEVEL_CHOICES = (
        (1, 'High'),
        (2, 'Moderate'),
        (3, 'Low')
    )
    type = models.CharField(max_length=255, choices=LEVEL_CHOICES, default=3)

    status = models.BooleanField(default=False)

