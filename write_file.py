#  coding:utf-8
import os


def write_file(success_url,filename):
    target_file = filename + ".html"
    with open("result/"+target_file,"w") as fp:
        for i in success_url:
            fp.write("<a href="+i+">"+i+"</a>")