from django.urls import path

from monitor.views import TaskProgressView

urlpatterns = [

    # 获取任务进度
    path('tasks/progress/', TaskProgressView.as_view()),

]