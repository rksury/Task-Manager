

from rest_framework.viewsets import ModelViewSet
# from rest_framework.permissions import IsAuthenticated, AllowAny

from task_manage.serializers import TaskSerializer, ProjectSerializers

class TaskViewSet(ModelViewSet):
    serializer_class = TaskSerializer

class ProjectViewSet(ModelViewSet):
    serializer_class = ProjectSerializers

    # def create_task(self, request, *args, **kwargs):
    #     create = super().create(request, *args, **kwargs)
    #     return create