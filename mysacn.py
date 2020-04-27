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
    with open("lib/PHP.txt", "r") as f:
        dir_str = f.readlines()
    dirstr = []
    for i in dir_str:
        dirstr.append(i.strip('\n'))
    return dirstr


def scan_dir(url, dirstr):
    target_url = "http://" + url + dirstr
    req = requests.get(target_url, timeout=1)
    print("scaning..",target_url)
    if req.status_code == 200:
        print(target_url)
        print("ok!")
        time.sleep(0.1)
    if re.match(req.status_code,"30.*?"):
        print()


#创建线程池
def manyThread(url,temp):
    threadlist = []
    for i in range(temp):
            t = Thread(target=scan_dir, args=(url,dir_str[i],))
            threadlist.append(t)
    for t in threadlist:
            t.start()


if __name__ == '__main__':
    try:
        argv = sys.argv
        url = parameter.parameter(argv)
        print(url)
        if url != None:
            temp=5
            dir_str = get_dir_asp()
            dir_len = len(dir_str)
            count = math.ceil(dir_len / temp)
            for j in range(count):
                manyThread(url,5)
    except KeyboardInterrupt:
        exit(0)
