from django.contrib import admin
from django.urls import path

from tasks.views import all_tasks_view, add_tasks_view, complete_task_view, completed_tasks_view
from tasks.views import delete_task_view, tasks_view

urlpatterns = [
    path("admin/", admin.site.urls),
    path("add-task/", add_tasks_view),
    path("all_tasks/", all_tasks_view),
    path("completed_tasks/", completed_tasks_view),
    path("complete_task/<int:task_id>/", complete_task_view),
    path("delete-task/<int:task_id>/", delete_task_view),
    path("tasks/", tasks_view)
]
