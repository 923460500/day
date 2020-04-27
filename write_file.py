#  coding:utf-8
import os


def write_file(success_url,filename,type):
    target_file = filename + type + ".html"
    if type == "sqli":
      #  with open("result/" + target_file, "w") as fp:
            #for i in
        pass
    elif type == "web":
        with open("result/" + target_file, "w") as fp:
            for i in success_url:
                fp.write("<a href="+i+">"+i+"</a>" + "<br/>")