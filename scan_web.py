# coding:utf-8

import requests
from threading import Thread
import re
import parameter
import sys
import user_agent_file
import time
import write_file

class scandir:
    def __init__(self,url):
        self.url = "http://"+url


    def open_file(self):
        with open("lib/test.txt", "r", encoding="utf-8") as fp:
            scan_str = fp.readlines()
            scanstr = []
            for i in scan_str:
                scanstr.append(i.strip('\n\t'))
        return scanstr

    def print_str(self):
        scan_str = self.open_file()
        agent = user_agent_file.get_user_agent()
        sucess_url = []
        for i in scan_str:
            target_url = self.url +i
            req = requests.get(url=target_url,timeout=1)
            print("scaning...",target_url)
            if req.status_code==200:
                print(target_url,"ok!")
                sucess_url.append(target_url)
                time.sleep(0.1)
            elif req.status_code == 302:
                print("so many try,exit")
                break
        print("write")
        write_file.write_file(sucess_url,"scan_web")


if __name__ == '__main__':
    url = parameter.parameter(sys.argv)
    print(url)
    if url != None:
        scan_str = scandir(url)
        scan_str.print_str()
