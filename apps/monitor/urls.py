from django.urls import path

from monitor.views import TaskProgressView

urlpatterns = [

    # tasks 列表清单？
    path('tasks/progress/', TaskProgressView.as_view()),

]