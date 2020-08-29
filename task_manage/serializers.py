from datetime import datetime, timezone

from rest_framework import serializers
from task_manage.models import Project, Task


class ProjectSerializers(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = "__all__"

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = "__all__"