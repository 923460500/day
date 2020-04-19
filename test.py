# coding:utf-8

import requests
import getopt
import sys

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