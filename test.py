# coding:utf-8

import requests
req=requests.get("http://127.0.0.1:8775/scan/12b3c2b27b03905f/log")
req_data=req.json()
print(type(req_data['log']))
for i in req_data:
    print(i)
    for j in req_data['success']:
        print(req_data['success'])
