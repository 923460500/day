# coding:utf-8

import requests
import getopt
import sys
import datetime


def usage():
    print("=====================")
    print("=======usage=========")
    print("=====================")

if __name__ == '__main__':
    target_ip, target_args = getopt.getopt(sys.argv[1:], "i:p:h")
    for name, value in target_ip:
        if name in ('-i'):
            print('vaule:{0}'.format(value))
        if name in ('-p'):
            print('port:{0}'.format(value))
        if name in ('-h'):
            print('this is usage'),usage()

    curr_time = datetime.datetime.now()
    time_str = curr_time.strftime("%Y%m%d")  # 获取当前时间，用来判断脚本是否有更新
    print(int(time_str))
    last_str = (datetime.datetime.now()+datetime.timedelta(days=-1)).strftime("%Y%m%d")
    print(last_str)
    test=open("C:\\Users\\Administrator\\Desktop\\test.sql","r")
    sql=[]
    for i in test.readlines():
        sql.append(i.strip('\n,\t'))
    print(sql)
    if "create table mysql" in sql:
        print("yes")