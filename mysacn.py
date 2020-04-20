# coding:utf-8

import requests
import sys
import parameter
import time
from threading import Thread
from time import sleep
import threading


def get_dir():
    with open("lib/ASP.txt", "r") as f:
        dir_str = f.readlines()
    dirstr = []
    for i in dir_str:
        dirstr.append(i.strip('\n'))
    return dirstr


def scan_dir(url, dirstr):
    print(dirstr)
    print(url)
    for i in dirstr:
        target_url = "http://"+url + i
        req = requests.get(target_url, timeout=1)
        print(target_url)
        if req.status_code == 200:
            print(target_url)
            print("ok!")
            time.sleep(0.1)


def manyThread(argv):
    threadlist = []
    url = parameter.parameter(argv)
    dir_str = get_dir()
    for i in range():
        t = Thread(target=scan_dir(),args=(url,dir_str))
        threadlist.append(t)
    for t in threadlist:
        t.start()


if __name__ == '__main__':
    argv = sys.argv
    scan_dir()
