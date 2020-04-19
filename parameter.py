# coding:utf-8
'''
这个文件是为了处理输入的参数，sys.argv有点不太好用。
多种注入会有太多重复代码
'''

import sys
import getopt


def parameter(argv):
    args, other = getopt.getopt(argv[1:], "u:p:h:D:C:", ["help", "table=", "column="])
    for name, value in args:
        if name in ('-h', '--help'):
            print("this is help:")
            print("[*]")
        if name in ('-u', '--url'):
            print("url:{0}".format(value))
            return format(value)
        if name in ('-D', '--database'):
            print("database:{0}".format(value))
            return format(value)
        if name in ('-C', '--column'):
            print("column:{0}".format(value))
            return format(value)
