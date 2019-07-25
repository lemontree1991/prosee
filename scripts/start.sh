#!/bin/bash
cd $HOME/projects/AlgorithmsSystem
source  $HOME/.virtualenvs/alg_env_test/bin/activate

uwsgi --ini uwsgi.ini
#uwsgi --reload xxx.pid
#uwsgi --stop xxx.pid

#celery multi start 2 -A AlgorithmsSystem -l info -c3
celery multi start 2 \
-A AlgorithmsSystem \
-l info \
--logfile=$HOME/projects/AlgorithmsSystem/log/%n%I.log \
--pidfile=$HOME/projects/AlgorithmsSystem/pids/%n.pid