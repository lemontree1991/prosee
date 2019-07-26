import json

from celery.result import AsyncResult
from django.http import JsonResponse
from django.shortcuts import render_to_response
from django.views import View

from expands.celery.client import CeleryClient


class TaskProgressView(View):
    def get(self,request):
        return render_to_response("index.html")

    def post(self, request):
        result = {
            "code": 400,
            "message": "错误的请求参数",
            "data": None
        }

        data = request.body.decode("utf-8")
        dict_data = json.loads(data)
        task_id = dict_data["task_id"]

        the_task = AsyncResult(task_id)
        if the_task.state == 'PROGRESS':
            resp = {'state': 'progress', 'progress': the_task.info.get('progress', 0)}
        elif the_task.state == 'SUCCESS':
            resp = {'state': "success", 'progress': 100}
        elif the_task.state == 'PENDING':  # 任务处于排队之中
            instance = CeleryClient()
            is_exist = False
            # 处于eta状态
            response = instance.scheduled_tasks()
            for k, v in response.items():
                for t in v:
                    if t["request"]["id"] == task_id:
                        is_exist = True
                        break
                else:
                    continue
                break
            if is_exist:

                resp = {'state': 'waitting', 'progress': 0}
            else:
                result["message"]= "task id不存在"
                return JsonResponse(result, status=404)
        else:
            resp = {'state': the_task.state, 'progress': 0}
        result["data"] = resp
        result["code"] = 200
        result["message"] = "查询成功"
        return JsonResponse(result, status=200)

