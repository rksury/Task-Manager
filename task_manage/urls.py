from django.conf.urls import url, include
from django.urls import path
from . import views


urlpatterns = [
    path('task', views.TaskList.as_view()),
    path('task', views.TaskDetail.as_view()),
]
