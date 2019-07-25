# -*- coding: UTF-8 -*-
import os

class BaseAlgorithm:
    """
    算法基类
    """

    # def __init__(self, task, name,args=None):
    #     self.name = name
    #     self.task = task
    #     self.args = args

    def __init__(self):
        self.__name = None
        self.__task = None
        self.__args = None
        self.__path = None

    @property
    def base_dir(self):
        return os.path.dirname(os.path.abspath(__file__))

    @property
    def path(self):
        return self.__path

    @path.setter
    def path(self,value):
        package_name = value.split(".")[2]
        self.__path = os.path.join(self.base_dir,package_name)

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def task(self):
        return self.__task

    @task.setter
    def task(self, value):
        self.__task = value

    @property
    def args(self):
        return self.__args

    @args.setter
    def args(self, value):
        self.__args = value


    def report(self, progress, state="PROGRESS"):
        self.task.update_state(state=state, meta={
            'progress': progress,

        })

    def __repr__(self):
        return self.name
