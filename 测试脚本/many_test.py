import sys
import time
import asyncio

import requests




async def do_test():
    url = create_task_url
    create_result =  requests.post(url, json=data).json()
    start_time = time.time()
    task_id= create_result["data"]["task_id"]
    while True:
        query_result =  requests.post(query_task_url, json={
            "task_id":task_id
        }).json()
        try:
            state = query_result["data"]["state"]
            progress = query_result["data"]["progress"]
        except KeyError as e:
            print(task_id+"排队中")
            await asyncio.sleep(0.5)
            start_time - time.time()
            continue
        print(f"task id: {task_id} 状态：{state} 进度：{progress}%")
        await asyncio.sleep(0.5)
        if state == "success":
            print(f"task id: {task_id} 执行结束 耗时{time.time()-start_time}")
            break


async  def main(n):
    await asyncio.gather(*[do_test() for i in range(n)])



if __name__ == '__main__':
    task_num = 4
    if len(sys.argv)==2:
        task_num = int(sys.argv[1])



    create_task_url = "http://192.168.2.129/monitor/tasks/"
    query_task_url ="http://192.168.2.129/monitor/tasks/status/"

    data = {'alg_id': '002', 'params': [30, 10], 'countdown': 0}

    s = time.time()

    asyncio.run(main(task_num))

    print(time.time()-s)
