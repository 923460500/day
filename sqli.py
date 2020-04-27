# coding:utf-8

import requests
import time
import json
from threading import Thread
import write_file

sqlapi_url = "http://127.0.0.1:8775"


class client():
    def __init__(self, admintoken="", taskid="", filepath=None):
        self.admintoken = admintoken
        self.sqlapi_url = sqlapi_url
        self.taskid = taskid
        self.status = ""
        self.scan_start_time = ""
        self.scan_end_time = ""
        self.engineid = ""
        self.filepath = ""
        self.headers = {'Content-Type': 'application/json'}

    def get_task_new(self):
        r = requests.get(url="%s/task/new" % (sqlapi_url))
        self.taskid = r.json()['taskid']
        if self.taskid != "":
            return self.taskid
        else:
            print("创建扫描任务失败！")
            return None

    def set_task_options(self, url):
        self.filepath = url

    def get_start_scan(self, url):
        r = requests.post(sqlapi_url + '/scan/' + self.taskid + '/start',
                          data=json.dumps({'url': url, 'getCurrentUser': True, 'getCurrentDb': True}),
                          headers=self.headers)
        if r.json()['success']:
            self.scan_start_time = time.time()
            # print(r.json())
            return r.json()['engineid']
        else:
            return None

    def get_scan_status(self):
        #   print(sqlapi_url + '/scan/' +self.taskid + '/status')
        #   print(requests.get(sqlapi_url + '/scan/' + self.taskid + '/status').json()['status'])
        self.status = requests.get(sqlapi_url + '/scan/' + self.taskid + '/status').json()['status']
        if self.status == 'terminated':
            self.scan_end_time = time.time()
            return True
        elif self.status == 'running':
            return False
        else:
            self.status = False

    def get_result(self):
        if self.status:
            r = requests.get(sqlapi_url + '/scan/' + self.taskid + '/data')
            if r.json()['data']:
                return r.json()['data']
            else:
                return None

    def get_scan_list(self):
        r = requests.get(self.sqlapi_url + '/admin/' + self.admintoken + '/list')
        if r.json()['success']:
            return r.json()['task']
        else:
            return None

    def del_a_task(self):
        r = requests.get(self.sqlapi_url + '/task/' + self.taskid + '/delete')
        if r.json()['success']:
            return True
        else:
            return False

    def stop_a_task(self):
        r = requests.get(self.sqlapi_url + '/scan/' + self.taskid + '/stop')
        if r.json()['success']:
            return True
        else:
            return False

    def flush_all_task(self):
        r = requests.get(self.sqlapi_url + '/admin/' + self.admintoken + '/flush')
        if r.json()['success']:
            return True
        else:
            return False

    def get_scan_log(self):
        r = requests.get(self.sqlapi_url + '/scan/' + self.taskid + '/log')
        return r.json()


def main():
    print('-' * 15 + "start working" + '-' * 15)
    target = "http://localhost:81/sqli/Less-1/"
    task1 = Thread(target=set_start_get_result, args=(target,))
    task1.start()


def time_deal(mytime):
    first_deal_time = time.localtime(mytime)
    second_deal_time = time.strftime("%Y-%m-%d %H:%M:%S", first_deal_time)
    return second_deal_time


def set_start_get_result(url):
    print(url)
    current_taskid = my_scan.get_task_new()
    print("task_id:", current_taskid)
    my_scan.set_task_options(url=url)
    print('扫描id:' + str(my_scan.get_start_scan(url=url)))
    print('扫描开始时间:' + str(time_deal(my_scan.scan_start_time)))
    while True:
        if my_scan.get_scan_status():
            scan_data = my_scan.get_result()
            print("当前数据库名：" + scan_data[-1]['value'])
            print("当前用户名" + scan_data[-2]['value'])
            print("数据库版本", scan_data[-3]['value'][0]['dbms_version'])
            print("扫描结束时间" + str(time_deal(my_scan.scan_end_time)))
            print("扫描日志" + type(my_scan.get_scan_log()))
            print('-' * 15 + "sql注入检测结束" + '-' * 15)
            break


if __name__ == '__main__':
    my_scan = client("1a3e1696122b26bc80161a886ca4dbd0")
    main()
