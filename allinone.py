# coding:utf-8
import click
from termcolor import cprint

import mysacn
import scan_web
import Struts2Scan
import parameter
import sys
import sqli
import dedescan

moudle_help = '''需要使用的检测模块，参数如下：\n
sqli：sql注入检测模块\n
adminscan：管理员目录扫描\n
dedescan：织梦漏洞检测\n
struts：struts2框架网站漏洞检测\n
webscan:危险目录检测\n
例如，需要使用sql注入检测模块，命令行中使用参数 -u 想要检测的url地址 -m sqli
'''

CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])


@click.command(context_settings=CONTEXT_SETTINGS)
@click.option('-u', '--url', help="需要检测的url")
@click.option('-m', '--moudle', help=moudle_help)
@click.option('-i', '--info', is_flag=True, help="漏洞信息介绍(以下帮助内容仅限于struts2框架漏洞检测使用:)")
@click.option('-n', '--name', help="指定漏洞名称, 漏洞名称详见info")
@click.option('-f', '--file', help="批量扫描URL文件, 一行一个URL")
@click.option('-c', '--encode', default="UTF-8", help="页面编码, 默认UTF-8编码")
@click.option('-t', '--timeout', help="HTTP超时时间, 默认10s")
@click.option('-w', '--workers', help="批量扫描进程数, 默认为10个进程")
@click.option('--header', help="HTTP请求头, 格式为: key1=value1&key2=value2")
@click.option('--Webpath', is_flag=True, help="获取WEB目录绝对路径")
@click.option('-q', '--quiet', is_flag=True, help="关闭打印不存在漏洞的输出，只保留存在漏洞的输出")
def main(url, moudle,info, file, name, header, encode, quiet, timeout,
         workers, webpath):
    argv = parameter.parameter(sys.argv)
    if argv:
        if moudle:
            if moudle == "sqli":
                my_scan=sqli.client("1a3e1696122b26bc80161a886ca4dbd0")
                sqli.sqli_start(url,my_scan)
            elif moudle == "adminscan":
                mysacn.mycan(url)
            elif moudle == "struts":
                try:
                    Struts2Scan.struts2(info, url, file, name, header, encode, quiet, timeout,
         workers, webpath)
                except KeyboardInterrupt as e:
                    pass
                except Exception as e:
                    click.secho("[ERROR] {error}".format(error=e), fg='red')
                    exit(0)
            elif moudle == "webscan":
                scan_web.scan_web()
            elif moudle == "dedescan":
                dedescan.dedescan(url)

        else:
            click.secho("ERROR:\n[*]未选择需要使用的模块",fg='red')

if __name__ == '__main__':
    main()
