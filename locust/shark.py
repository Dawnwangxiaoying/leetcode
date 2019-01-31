from locust import HttpLocust, TaskSet
import random

with open('./shark.txt', 'r') as f:
    data = f.readlines()
    list = []
    for line in data:
        list.append(line.replace("\n", ""))
    print (list)
    # q = queue.Queue()
    # q.put(list)
    # print(q.get())


# def getstatus(l):
#     l.client.get("/happy/shake/user/rank?name="+random.choice(list) )
#     # print(info.json())
#
# def shark(l):
#
#     data = {"name": random.choice(list), "groupName": "555"}
#     info = l.client.post("/happy/shake/score", json=data)
#     try :
#         assert info.json()["isSuccess"]
#     except:
#         pass
#         # logging.info(info.text)
#         print(info.json())
#
#
#     # isPassed = info.ok
#     # assert isPassed
#
# class UserBehavior(TaskSet):
#     tasks = {shark: 3, getstatus: 1}
#
#     def on_start(self):
#         shark(self)
#
#
# class WebsiteUser(HttpLocust):
#     task_set = UserBehavior
#     min_wait = 1
#     max_wait = 1
