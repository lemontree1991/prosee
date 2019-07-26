from django.urls import path

from monitor.views import TaskProgressView,WorkerStatusView,AlgorithmLibView,TaskIndexView

urlpatterns = [

    # 获取任务进度
    path('tasks/progress/', TaskProgressView.as_view(),name="tasks_progress"),
    # worker 状态
    path('workers/status/', WorkerStatusView.as_view(),name="workers_status"),
    # 算法库
    path('algorithms/', AlgorithmLibView.as_view(),name="algorithms"),
    # 任务首页
    path('tasks/index/', TaskIndexView.as_view(),name="task_index"),
]