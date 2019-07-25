import json
import logging
from json import JSONDecodeError

from django.http import JsonResponse
from django.views import View

from core.algorithms.algorithmLibrary import AlgorithmLibrary
from .tasks import execute_algorithm

logger = logging.getLogger(__name__)


class TasksCreateView(View):

    def post(self, request):
        result = {
            "code":400,
            "message":"错误的请求参数",
            "data":None
        }

        data = request.body.decode("utf-8")
        is_valid = True
        try:

            dict_data = json.loads(data)
            alg_id = dict_data["alg_id"]
            params = dict_data["params"]
            countdown = int(dict_data.get("countdown",0))

        except Exception as e:
            is_valid = False
            if isinstance(e,JsonResponse):
                result["message"] = "错误的请求格式"
            elif isinstance(e,KeyError):
                result["message"] = "缺少必要参数"
            elif isinstance(e,ValueError):
                result["message"] = "错误的参数数据类型"
            else:
                result["message"] = "未知错误"

        if not is_valid:
            return JsonResponse(
                data=result, safe=False,status=400
            )


        info = AlgorithmLibrary.get_algorithm_by_id(alg_id)
        if not info:
            result["message"] = "算法不存在"
            return JsonResponse(
                data=result, safe=False
            )

        alg_class, alg_name, package_path = info
        task = execute_algorithm.apply_async(args=params, kwargs={
            "alg_class": alg_class,
            "alg_name": alg_name,
            "package_path": package_path,

        }, countdown=countdown)
        result["data"] = {
            "task_id":task.id
        }

        result["message"] = "成功"
        return JsonResponse(
            data=result, safe=False
        )

