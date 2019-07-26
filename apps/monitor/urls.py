from django.urls import path

from monitor.views import TaskProgressView,WorkerStatusView

urlpatterns = [

    # 获取任务进度
    path('tasks/progress/', TaskProgressView.as_view(),name="tasks_progress"),
    # worker 状态
    path('workers/status/', WorkerStatusView.as_view(),name="workers_status"),

]