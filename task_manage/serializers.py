from rest_framework import serializers
from task_manage.models import TaskEntry

class TaskSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(required=False, allow_blank=True, max_length=100)

    def create(self, validated_data):
        return TaskEntry.objects.create(**validated_data)
