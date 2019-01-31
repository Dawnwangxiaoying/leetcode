from locust import HttpLocust, TaskSet,task
import random
import requests

randomtoken = True
host = "https://pre.alphalawyer.cn/"

def getaccount(path = "/Users/icourt2/Desktop/test/locust3.6/available.txt"):
    with open(path, 'r') as f:
        account = []
        for line in f.readlines():
            account.append(line.replace("\n", ""))
    return account

def login(account):
    tokens = []
    for username in account:
        url = host + "ilaw/api/v1/auth/login"
        data = {"user": username, "password": "123456", "deviceType": "web"}
        headers = {"Content-Type": "application/json;charset=UTF-8"}
        r = requests.post(url, json=data, headers=headers)
        tokens.append(r.json()["token"])
    return tokens

if randomtoken:
    account = getaccount()
tokens = login(account)
# print(tokens)

def matters(l):
    data ={"matterType":78860,"childMatterType":{"id":78860,"name":"民事诉讼","code":"民事诉讼","remark":"","enable":"true","parentId":78856,"displayOrder":1,"typeOfParentMatterType":0},"name":"压力测试2018-08-13","matterNo":"","level":"1","needAppro":"false","status":"0","hasProjectNumberRole":"false","groups":[],"clients":[{"contactPkid":"5C48B103858611E8A89E6C92BF3BB0F7"}],"litigants":[],"relevants":[],"members":[{"userId":"76CA95EB84E811E8AD526C92BF3B5CD5","roleId":135421},{"userId":"EBEF0D649EAC11E8BBAB1051721C38E2","roleId":135422},{"userId":"F34984559EAC11E8BBAB1051721C38E2","roleId":135422},{"userId":"C2C712739EAC11E8BBAB1051721C38E2","roleId":135422},{"userId":"FB058CC79EAC11E8BBAB1051721C38E2","roleId":135422},{"userId":"0C2BCB34963A11E8BBAB1051721C38E2","roleId":135422},{"userId":"D06ACEDA9EAC11E8BBAB1051721C38E2","roleId":135422},{"userId":"D5EE09E59EAC11E8BBAB1051721C38E2","roleId":135422},{"userId":"DB9FCAEA9EAC11E8BBAB1051721C38E2","roleId":135422},{"userId":"E0AC9FD99EAC11E8BBAB1051721C38E2","roleId":135422},{"userId":"E6C95FE69EAC11E8BBAB1051721C38E2","roleId":135422},{"userId":"8D0AC535858611E8A89E6C92BF3BB0F7","roleId":135422}],"originatingAttorneys":[{}]}
    headers = {"token":random.choice(tokens)}
    info = l.client.post("/ilaw/api/v1/matters", json=data,headers=headers)
    print(info.json())
    try :
        assert info.json()["项目创建成功"]
    except:
        pass
        print(info.json())

class UserBehavior(TaskSet):
    tasks = {matters: 1}


class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    min_wait = 1
    max_wait = 2

