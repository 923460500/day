# coding:utf-8
'''
这个文件是为了处理输入的参数，sys.argv有点不太好用。
多种注入会有太多重复代码
'''

import sys
import getopt
import logging

logging.basicConfig(level=logging.INFO,format='%(asctime)s - %(levelname)s:%(message)s')

def parameter(argv):
    args, other = getopt.getopt(argv[1:], "u:p:hD:C:", ["help", "table=", "column="])
    err_msg= '''参数输入错误
[*]使用-h --help 获取帮助
'''
    help_msg = '''
********************************
*******this is help*************
********************************
[*]-h --help 获取帮助
[*]-u --url 指定需要检测的url或者ip
[*]-o  其他帮助
'''
    if not args:                    # 参数为空
         logging.error(err_msg)
    for name, value in args:
        if name in ('-h', '--help'):
            logging.info(help_msg)
        if name in ('-u', '--url'):
            return format(value)
        if name in ('-D', '--database'):
            return format(value)
        if name in ('-C', '--column'):
            return format(value)
