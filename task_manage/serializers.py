from string import Template

from django.utils import timezone
from rest_framework import serializers

from task_manage.models import Project, Task


class DeltaTemplate(Template):
    delimiter = "%"


def strfdelta(tdelta, fmt):
    d = {"D": tdelta.days}
    hours, rem = divmod(tdelta.seconds, 3600)
    minutes, seconds = divmod(rem, 60)
    d["H"] = '{:02d}'.format(hours)
    d["M"] = '{:02d}'.format(minutes)
    d["S"] = '{:02d}'.format(seconds)
    t = DeltaTemplate(fmt)
    return t.substitute(**d)


class ProjectSerializers(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = "__all__"


class TaskSerializer(serializers.ModelSerializer):
    remaining_time = serializers.SerializerMethodField()

    class Meta:
        model = Task
        fields = "__all__"

    def get_remaining_time(self, obj):
        return strfdelta(obj.end_time - timezone.now(), '%H:%M:%S')
