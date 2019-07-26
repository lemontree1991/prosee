# -*- coding: UTF-8 -*-
from os import cpu_count

# Broker配置，使用Redis作为消息中间件


CELERY_BROKER_URL = "redis://localhost:6379/1"
# BACKEND配置
CELERY_RESULT_BACKEND = "redis://localhost:6379/2"

# 导入目标任务文件
CELERY_IMPORTS = (
    "apis.tasks",
)

CELERY_QUEUES = {
    "default_queue": {  # 这是上面指定的默认队列
        "exchange": "default_queue",
        "exchange_type": "direct",
        "routing_key": "default_queue"
    },
    "topic_queue": {  # 这是一个topic队列 凡是topic_test开头的routing key都会被放到这个队列
        "routing_key": "topic_test.#",
        "exchange": "topic_exchange",
        "exchange_type": "topic",
    },
    "beat_queue": {  # 定时任务
        "exchange": "beat_queue",
        "exchange_type": "direct",
        "binding_key": "beat_queue",
    },
    "work_queue": {  # 异步任务
        "exchange": "work_queue",
        "exchange_type": "direct",
        "binding_key": "work_queue",
    },

    "test2": {  # test和test2是2个fanout队列,注意他们的exchange相同
        "exchange": "broadcast_tasks",
        "exchange_type": "fanout",
        "binding_key": "broadcast_tasks",
    },
    "test": {
        "exchange": "broadcast_tasks",
        "exchange_type": "fanout",
        "binding_key": "broadcast_tasks2",
    },
}

CELERY_TASK_DEFAULT_QUEUE = "default_queue"

# 任务序列化方案
CELERY_TASK_SERIALIZER = 'pickle'
# 结果序列化方案
CELERY_RESULT_SERIALIZER = 'json'
# 指定任务接受的序列化类型
CELERY_ACCEPT_CONTENT = ['json', 'pickle']

# 防止死锁 无效
# CELERYD_FORCE_EXECV = True

# 设置worker的并发数
# celery worker的并发数 也是命令行-c指定的数目,事实上实践发现并不是worker也多越好,保证任务不堆积,加上一定新增任务的预留就可以
CELERY_WORKER_CONCURRENCY = cpu_count() - 1

# celery worker 每次预取任务的数量
CELERYD_PREFETCH_MULTIPLIER = cpu_count() - 1

# 允许重试
CELERY_ACKS_LATE = True

#  每个worker最多执行100个任务就会被销毁，可防止内存泄露
# 建议数量可以大一些，比如200
CELERYD_MAX_TASKS_PER_CHILD = 100

# 单个任务最大运行时间,超时worker会被杀死,并将任务交给主进程 单位秒
CELERYD_TASK_TIME_LIMIT = 30 * 60 * 10

# 设置时区
CELERY_TIMEZONE = 'Asia/Shanghai'
# utc禁用
CELERY_ENABLE_UTC = False

# 压缩方案选择，可以是zlib, bzip2，默认是发送没有压缩的数据
CELERY_MESSAGE_COMPRESSION = 'zlib'
