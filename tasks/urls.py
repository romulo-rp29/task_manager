from django.urls import path
from tasks.views import index
from tasks import views


urlpatterns = [
    path("", index, name="home-page"),
    path("tasks/", views.tasks_list, name="tasks_list"),
    path("create/", views.create_task, name="create_task"),
    path("task/<int:task_id>/edit/", views.edit_task, name="edit_task"),
    path("task/<int:task_id>/delete/", views.delete_task, name="delete_task"),
    path(
        "task/<int:task_id>/toggle/",
        views.toggle_task_completion,
        name="toggle_task_completion",
    ),
]
