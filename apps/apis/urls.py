# -*- coding: UTF-8 -*-
from django.urls import path

from .views.tasks import TasksCreateView

urlpatterns = [

    # tasks 列表清单？
    path('tasks/', TasksCreateView.as_view()),

]