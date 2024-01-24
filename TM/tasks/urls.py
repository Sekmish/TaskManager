from django.urls import path
from .views import task_list, task_create, task_delete, task_edit, completed_task_list
from . import views

urlpatterns = [
    path('', task_list, name='task_list'),
    path('create/', task_create, name='task_create'),
    path('delete/<int:id>/', task_delete, name='task_delete'),
    path('edit/<int:id>/', task_edit, name='task_edit'),
    path('completed_tasks/', completed_task_list, name='completed_task_list'),
    path('task/return/<int:id>/', views.task_return, name='task_return'),
    ]