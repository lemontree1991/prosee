#!/bin/bash
cd $HOME/projects/AlgorithmsSystem
source  $HOME/.virtualenvs/alg_env_test/bin/activate


pkill -9 -f 'celery worker'
celery multi start 1 -A AlgorithmsSystem -l info -c3
uwsgi --reload pids/uwsgi.pid

nginx -s reload