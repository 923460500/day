# coding:utf-8

import requests
import getopt
import sys
import parameter


def get_url_help(argv):
    print(argv)
    target_ip,args=getopt.getopt(argv[1:],"u:p:h",['help','url=','version:'])
    print("target_ip:",target_ip)
    print("args:",args)
    for name,value in target_ip:
        print(name)
        if name in ('-u','--url'):
            print("url:{0}".format(value))
            target_ip=name
        if name in ('-p'):
            print('p:{0}'.format(value))
        if name in ('-h'):
            print('help:{0}'.format(value))
    print(target_ip)


if __name__ == '__main__':
    argv=sys.argv
    print(type(argv))
    #print(argv)
    get_url_help(sys.argv)