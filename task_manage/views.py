from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny

# class TaskList(GenericAPIView):
#     permission_classes = (IsAuthenticated, AllowAny)
#
#     def get(self, request):
#         return task_services.get_task(request.data)
#
#     def post(self, request, format=None):
#         return task_services.create_task(request.data)
#
# class TaskDetail(GenericAPIView):
#     permission_classes = (IsAuthenticated, AllowAny)
#
#     def get(self, request, task_id, format=None):
#         return task_service.get_task(request.user, task_id)
#
#     def put(self, request, task_id, format=None):
#         return task_service.update_task(request.user, task_id, request.data)
#
#     def delete(self, request, task_id, format=None):
#         return task_service.delete_task(request.user, task_id)


