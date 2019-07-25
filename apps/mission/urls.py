# -*- coding: UTF-8 -*-
from django.urls import path

from .views import TasksCreateView

urlpatterns = [

    # tasks 列表清单？
    path('', TasksCreateView.as_view()),

]