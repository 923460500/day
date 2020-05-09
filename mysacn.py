# coding:utf-8

import requests
import sys
import parameter
import time
from threading import Thread
from time import sleep
import threading
import math
import re
import write_file
import os

def get_dir_asp():
    with open("lib/ASP.txt", "r") as f:
        dir_str = f.readlines()
    dirstr = []
    for i in dir_str:
        dirstr.append(i.strip('\n'))
    return dirstr


def get_dir_aspx():
    with open("lib/ASPX.txt", "r") as f:
        dir_str = f.readlines()
    dirstr = []
    for i in dir_str:
        dirstr.append(i.strip('\n'))
    return dirstr


def get_dir_jsp():
    with open("lib/JSP.txt", "r") as f:
        dir_str = f.readlines()
    dirstr = []
    for i in dir_str:
        dirstr.append(i.strip('\n'))
    return dirstr


def get_dir_php():
    with open("lib/test.txt", "r") as f:
        dir_str = f.readlines()
    dirstr = []
    for i in dir_str:
        dirstr.append(i.strip('\n'))
    return dirstr


def scan_dir(url, dir_str):
    success_url = []
    count = 0
    for i in dir_str:
        target_url = "http://" + url + i
        req = requests.get(url=target_url, timeout=1)
        if len(success_url) !=0:
            for j in success_url:
                print(j,"可能是危险的管理员登录路径！！！")
        print("scaning..")
        if req.status_code == 200:
            print(target_url)
            success_url.append(target_url)
            time.sleep(0.1)
        if req.status_code == 302:
            print(target_url,"链接被拒绝！")
            exit(0)
        count +=1
        if count%7 == 0:
            os.system('cls')
    if len(success_url) != 0:
     #   write_file.write_file(success_url, "admin", "web")
        print("扫描结束，结果已写入result目录下adminweb.html!")
    else:
        print(url,"没有找到管理员路径")


#创建线程池
#def manyThread(url,temp):
 #   threadlist = []
 #   for i in range(temp):
        #    t = Thread(target=scan_dir, args=(url,dir_str[i],))
        #    threadlist.append(t)
 #   for t in threadlist:
     #       t.start()


def mycan(url):
    print('-' * 15 + "管理员目录检测开始" + '-' * 15)
    try:
        if url != None:
            temp=5
            dir_str = get_dir_php()
            dir_len = len(dir_str)
            count = math.ceil(dir_len / temp)
            scan_dir(url,dir_str)
    except KeyboardInterrupt:
        exit(0)
    print('-' * 15 + "管理员目录检测结束" + '-' * 15)
