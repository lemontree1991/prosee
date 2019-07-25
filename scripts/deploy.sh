#!/bin/bash

if [ ! -d "$HOME/projects" ];then
echo "$HOME/projects不存在，创建$HOME/projects"
mkdir $HOME/projects
fi


if [ -d "$HOME/projects/AlgorithmsSystem" ];then
rm -rf $HOME/projects/AlgorithmsSystem
echo ************************************
fi
cd $HOME/projects && git clone https://gitee.com/leipeng1025/AlgorithmsSystem.git


if [ ! -d "$HOME/.virtualenvs" ];then
mkdir $HOME/.virtualenvs
fi

if [ -d "$HOME/.virtualenvs/alg_env_test" ];then
rm -rf $HOME/.virtualenvs/alg_env_test
echo ************************************
fi

python -m venv $HOME/.virtualenvs/alg_env_test

source  $HOME/.virtualenvs/alg_env_test/bin/activate

cd $HOME/projects/AlgorithmsSystem && pip install -r requirements.txt


python manage.py migrate

python manage.py loaddata initial_data.json