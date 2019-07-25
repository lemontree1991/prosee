# -*- coding: UTF-8 -*-
import importlib
import json
import logging

from algorithm.models import Algorithm
from expands.singleton import Singleton

logger = logging.getLogger("default")

class AlgorithmLibrary(Singleton):
    """
    算法库，包含所有算法
    """

    @staticmethod
    def get_algorithm_by_id(alg_id):

        try:
            alg = Algorithm.objects.get(id=alg_id)
            package_path = alg.path
            class_name = alg.class_name
            alg_name = alg.name
            # 获取算法类
            package = importlib.import_module(package_path)
            alg_class = getattr(package, class_name)
            return (alg_class, alg_name, package_path)
        except ModuleNotFoundError as e:
            logger.error(e)
        except AttributeError as e:
            logger.error(e)
        except Algorithm.DoesNotExist:
            logger.warning(f"Algorithm id is {alg_id} in db does not exist")
            return False
        return False
