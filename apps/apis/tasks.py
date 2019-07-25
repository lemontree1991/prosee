# -*- coding: UTF-8 -*-
import logging

from celery import Task, shared_task
from celery.exceptions import Ignore

logger = logging.getLogger(__name__)


class BaseTask(Task):
    track_started = True
    serializer = "pickle"

    def on_success(self, retval, task_id, args, kwargs):
        logger.info('{0!r} success'.format(task_id))

    def on_failure(self, exc, task_id, args, kwargs, einfo):
        logger.error('{0!r} failed: {1!r}'.format(task_id, exc))

    def on_retry(self, exc, task_id, args, kwargs, einfo):
        logger.warning('{0!r} retried: {1!r}'.format(task_id, exc))


@shared_task(base=BaseTask, bind=True, name="execute_algorithm_task")
def execute_algorithm(self, *args, **kwargs):
    task_id = self.request.id
    logger.info(f"task {task_id} received args:{args} kwargs:{kwargs}")

    alg_class = kwargs["alg_class"]
    alg = alg_class()
    # 设置算法属性
    alg.name = kwargs["alg_name"]
    alg.path = kwargs["package_path"]
    alg.task = self
    alg.args = args

    try:
        if not alg.init():
            self.update_state(state="INIT_ERROR")
            logger.error(f"task {task_id} init failed")
            raise Ignore()
        if not alg.dowork():
            self.update_state(state="DOWORK_ERROR")
            logger.error(f"task {task_id} dowork failed")
            raise Ignore()
        if not alg.finish():
            self.update_state(state="FINISH_ERROR")
            logger.error(f"task {task_id} finish failed")
            raise Ignore()

    except Exception as e:
        if not isinstance(e, Ignore):
            raise self.retry(countdown=10, max_retries=2, exc=e)
        else:
            raise Ignore()
