from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

from rest_framework import routers
router = routers.SimpleRouter(trailing_slash=False)

# from django.conf.urls import url, include
from task_manage.modelviewset import TaskViewSet, ProjectViewSet

router.register(r'^task', TaskViewSet, basename='create-task')
router.register(r'^project', ProjectViewSet, basename='create-project')

urlpatterns = [
]
urlpatterns += format_suffix_patterns(router.urls)
