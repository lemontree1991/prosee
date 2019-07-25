# -*- coding: UTF-8 -*-
from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'prosee.settings')

app = Celery('prosee')

# 大写的名称空间意味着必须以大写而不是小写来指定所有Celery配置选项，并以...开头 CELERY_，
# 例如task_always_eager设置变为CELERY_TASK_ALWAYS_EAGER
app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()
